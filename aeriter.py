import ConfigParser
import boto
from boto.s3.key import Key
import glob
import errno
from bottle import template, TEMPLATE_PATH
import os
import sys
import re
import markdown2
import shutil
from datetime import datetime
import cgi

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def main():
    # Set global variables from the command line
    global blogFolder
    global s3Bucket
    
    blogFolder = sys.argv[1]
    s3Bucket = sys.argv[2]
    
    # For any folders that are reserved by Aeriter
    if blogFolder == "templates":
        exit()

    # Read configuration for the blog
    global config
    config = ConfigParser.ConfigParser()
    config.read(blogFolder + '/settings.cfg')
    # You'll want to do this at the beginning of the process
    shutil.rmtree(blogFolder + '/rendered', ignore_errors=True)
    make_sure_path_exists(blogFolder + '/rendered')
    # This processes the individual .md files and places them in the "rendered" folder under
    # their respective relative paths.
    global postMetaData
    postMetaData = []
    for file in glob.glob(blogFolder + "/*.md"):
        if file[-9:] == '-draft.md':
            continue
        postMetaData.append(renderPost(file, blogFolder, config))
    genNavPages(postMetaData, blogFolder, config)
    sendToS3(s3Bucket, blogFolder)

def sendToS3(s3Bucket, blogFolder, logging_bucket='aeriter-logging', rendered='rendered'):
    conn = boto.connect_s3()
    nonexistent = conn.lookup(s3Bucket)
    if nonexistent is None:
        bucket = conn.create_bucket(s3Bucket)
    else:
        bucket = conn.get_bucket(s3Bucket)
    # Make sure you want to change this if you don't want to be sending me your log files!
    bucket.enable_logging(
        target_bucket=logging_bucket,
        target_prefix=bucket.name)
    bucket.configure_website(suffix='index.html')
    bucketKey = Key(bucket)
    myFolder = blogFolder + "/%s" % rendered
    for root, subdir, file in os.walk(myFolder):
        relDir = root.replace(myFolder, "", 1)
        for name in file:
            fileName = relDir + "/" + name
            bucketKey.key = fileName
            bucketKey.set_contents_from_filename(myFolder + "/" + fileName, policy='public-read')

"""Pass the meta data for all posts into this function, and
the front page, 2nd page, etc will be generated and placed in
the "rendered" folder appropriately.
"""
def genNavPages(postMetaData, blogFolder, config, rendered='rendered'):
    # We want to first sort the posts from newest to oldest.
    postMetaData.sort(key=lambda x: x[0], reverse=True)
    renderedPost = template('%s/page' % config.get("Settings", "theme"), postMetaData=postMetaData, config=config)
    make_sure_path_exists(blogFolder + '/%s/' % rendered)
    f = open(blogFolder + '/%s/' % rendered + '/index.html', 'w+')
    renderedPost = renderedPost.encode('ascii', 'xmlcharrefreplace')
    f.write(renderedPost)
    f.close()
    
    # We also want to make sure the template resources are available!
    copyanything("views/%s/resources" % config.get("Settings", "theme"), "%s/%s/resources" % (blogFolder, rendered))

"""Pass a .txt file from the blog to this function and
receive meta-data for the post.
The post itself will be rendered into HTML and placed
in the appropriate folder.
"""
def renderPost(postName, blogFolder, config, rendered='rendered'):
    # Obviously this will be abstracted out later
    f = open(postName, 'r')
    post = f.read()
    post = post.decode('utf-8')
    f.close()
    
    # all our fun, regexy matches
    titlematch = re.compile(r'\[title\]\n')
    relpathmatch = re.compile(r'\[relpath\]\n')
    datematch = re.compile(r'\[date\]\n')
    tagsmatch = re.compile(r'\[tags\]\n')
    authormatch = re.compile(r'\[author\]\n')
    postmatch = re.compile(r'\[post\]\n')
    linematch = re.compile('^.*$', re.M)
    
    postTitle = linematch.match(post, titlematch.search(post).end()).group(0)
    relpath = linematch.match(post, relpathmatch.search(post).end()).group(0)
    date = datetime.strptime(linematch.match(post, datematch.search(post).end()).group(0), "%Y-%m-%d-%H:%M")
    tags = linematch.match(post, tagsmatch.search(post).end()).group(0).split(',')
    author = linematch.match(post, authormatch.search(post).end()).group(0)
    post = cgi.escape(post[postmatch.search(post).end():])
    postGist = post[0:140] + '...'
    
    renderedPost = template('%s/template' % config.get("Settings", "theme"), postTitle=postTitle, post=markdown2.markdown(post), date=date, author=author, postGist=postGist.replace("\n", " "), config=config, tags=tags)
    make_sure_path_exists(blogFolder + '/' + rendered + '/' + relpath)
    f = open(blogFolder + '/' + rendered + '/' + relpath + '/index.html', 'w+')
    renderedPost = renderedPost.encode('ascii', 'xmlcharrefreplace')
    f.write(renderedPost)
    f.close()
    return (date, postTitle, relpath, tags, author, postGist)

if __name__ == '__main__':
    main()

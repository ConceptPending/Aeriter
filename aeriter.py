import ConfigParser
import boto
from boto.s3.key import Key
import glob
import errno
from bottle import template
import os
import sys
import re
import markdown2
import shutil
from datetime import datetime
import cgi

# Set global variables from the command line
blogFolder = sys.argv[1]
s3Bucket = sys.argv[2]

# For any folders that are reserved by Aeriter
if blogFolder == "templates":
    exit()

# Read configuration for the blog
config = ConfigParser.ConfigParser()
config.read(blogFolder + '/settings.cfg')

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

# all our fun, regexy matches
titlematch = re.compile(r'\[title\]\n')
relpathmatch = re.compile(r'\[relpath\]\n')
datematch = re.compile(r'\[date\]\n')
tagsmatch = re.compile(r'\[tags\]\n')
authormatch = re.compile(r'\[author\]\n')
postmatch = re.compile(r'\[post\]\n')
linematch = re.compile('^.*$', re.M)


# You'll want to do this at the beginning of the process
shutil.rmtree(blogFolder + '/rendered', ignore_errors=True)
make_sure_path_exists(blogFolder + '/rendered')

def main():
    # This processes the individual .md files and places them in the "rendered" folder under
    # their respective relative paths.
    postMetaData = []
    for file in glob.glob(blogFolder + "/*.md"):
        if file[-9:] == '-draft.md':
            continue
        postMetaData.append(renderPost(file))
    genNavPages(postMetaData)
    sendToS3()

def sendToS3():
    conn = boto.connect_s3()
    nonexistent = conn.lookup(s3Bucket)
    if nonexistent is None:
        bucket = conn.create_bucket(s3Bucket)
    else:
        bucket = conn.get_bucket(s3Bucket)
    bucketKey = Key(bucket)
    myFolder = blogFolder + "/rendered"
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
def genNavPages(postMetaData):
    # We want to first sort the posts from newest to oldest.
    postMetaData.sort(key=lambda x: x[0], reverse=True)
    #pageHTML = ""
    #for post in postMetaData:
    #    pageHTML += """
    #    <h2><a href="%s/">%s</a></h2>
    #    <p><span class="author">%s</span> - <span class="date">%s</span></p>
    #    <p>%s<a href="%s/">... [continue reading]</a></p>
    #    """ % (post[2], post[1], post[4], post[0], post[5][:-3], post[2])
    #print pageHTML
    renderedPost = template('templates/page', postMetaData=postMetaData, config=config)
    make_sure_path_exists(blogFolder + '/rendered/')
    f = open(blogFolder + '/rendered/' + '/index.html', 'w+')
    renderedPost = renderedPost.encode('ascii', 'xmlcharrefreplace')
    f.write(renderedPost)
    f.close()

"""Pass a .txt file from the blog to this function and
receive meta-data for the post.
The post itself will be rendered into HTML and placed
in the appropriate folder.
"""
def renderPost(postName):
    # Obviously this will be abstracted out later
    f = open(postName, 'r')
    post = f.read()
    post = post.decode('utf-8')
    f.close()

    postTitle = linematch.match(post, titlematch.search(post).end()).group(0)
    relpath = linematch.match(post, relpathmatch.search(post).end()).group(0)
    date = datetime.strptime(linematch.match(post, datematch.search(post).end()).group(0), "%Y-%m-%d-%H:%M")
    tags = linematch.match(post, tagsmatch.search(post).end()).group(0).split(',')
    author = linematch.match(post, authormatch.search(post).end()).group(0)
    post = cgi.escape(post[postmatch.search(post).end():])
    postGist = post[0:140] + '...'

    renderedPost = template('templates/template', postTitle=postTitle, post=markdown2.markdown(post), date=date, author=author, postGist=postGist.replace("\n", " "), config=config)
    os.chdir(blogFolder)
    make_sure_path_exists('rendered/' + relpath)
    f = open('rendered/' + relpath + '/index.html', 'w+')
    renderedPost = renderedPost.encode('ascii', 'xmlcharrefreplace')
    f.write(renderedPost)
    f.close()
    os.chdir(os.pardir)
    return (date, postTitle, relpath, tags, author, postGist)

if __name__ == '__main__':
    main()

import glob
import errno
from bottle import template
import os
import sys
import re
import markdown2
import shutil

blogFolder = sys.argv[1]

# For any folders that are reserved by Aeriter
if blogFolder == "templates":
	exit()

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

# all our fun, regexy matches
titlematch = re.compile('-title-\n')
relpathmatch = re.compile('-relpath-\n')
tagsmatch = re.compile('-tags-\n')
authormatch = re.compile('-author-\n')
postmatch = re.compile('-post-\n')
linematch = re.compile('^.*$', re.M)


# You'll want to do this at the beginning of the process
shutil.rmtree(blogFolder + '/rendered')
make_sure_path_exists(blogFolder + '/rendered')

def main():
	# This processes the individual .md files and places them in the "rendered" folder under
	# their respective relative paths.
	os.chdir(blogFolder)
	for file in glob.glob("*.md"):
		print renderPost(file)

# Pass a .txt file from the blog to this function and
# receive meta-data for the post.
# The post itself will be rendered into HTML and placed
# in the appropriate folder.
def renderPost(postName):
	# Obviously this will be abstracted out later
	f = open(postName, 'r')
	post = f.read()
	f.close()

	postTitle = linematch.match(post, titlematch.search(post).end()).group(0)
	relpath = linematch.match(post, relpathmatch.search(post).end()).group(0)
	tags = linematch.match(post, tagsmatch.search(post).end()).group(0).split(',')
	author = linematch.match(post, authormatch.search(post).end()).group(0)
	post = post[postmatch.search(post).end():]
	postGist = post[0:150] + '...'

	"""I'm going to assume there's no malicious HTML/JS for now.
	You are uploading your own .txt's after all.
	"""
	os.chdir(os.pardir)
	renderedPost = template('templates/template', postTitle=postTitle, post=markdown2.markdown(post), author=author, postGist=postGist.replace("\n", " "))
	os.chdir(blogFolder)
	make_sure_path_exists('rendered/' + relpath)
	f = open('rendered/' + relpath + '/index.html', 'w+')
	f.write(renderedPost)
	f.close()
	return (postTitle, relpath, tags, author, postGist)

if __name__ == '__main__':
	main()

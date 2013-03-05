Aeriter
=======

This will generate a static site and upload it to Amazon S3.

The utility takes a folder of .md files and generates a blog based on the template you've specified.

Currently, the only template is a plain-text template, and there's no way to save blog settings. However, those are the next two items on my to-do list.

You can render a blog with the following command:
	python aeriter.py <name of folder with you .md files> <name of Amazon S3 bucket>

You'll need to store your AWS access key and secret key using either environment variables or a Boto configuration file, as specified by the Boto documentation.

If the AWS bucket doesn't exist, it will be created.

Currently the folder with the posts must be located inside the Aeriter folder, but this will change in the future.

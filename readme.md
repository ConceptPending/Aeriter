Aeriter
=======

This will generate a static site and upload it to Amazon S3.

The utility takes a folder of .md files and generates a blog based on the template you've specified.

The files must end in ".md" and be in the following format:

    [title]
    <title of blog bost>
    [relpath]
    <relative path of blog post>
    [date]
    <publish date of post in "yyyy-mm-dd-HH:MM" format>
    [tags]
    <comma separated list of tags>
    [author]
    <name of author of the post>
    [post]
    <all post content in MarkDown format. This will be HTML escaped when rendered before uploading>

A filename with '-draft' appending before the extension (example: 'post1-draft.md') will be ignored during processing.

You must also have a "settings.cfg" file in the same folder in the following format:

    [Settings]
    title=<title of blog>
    description=<Meta description for front page>
    theme=<theme name, default is default>

Currently, there is only one template, but this will change in the future. This, among other things, will be included in the settings file.

You can render a blog with the following command:

    python aeriter.py <name of folder with you .md files> <name of Amazon S3 bucket>

You'll need to store your AWS access key and secret key using either environment variables or a Boto configuration file, as specified by the Boto documentation.

If the AWS bucket doesn't exist, it will be created.

Currently the folder with the posts must be located inside the Aeriter folder, but this will change in the future.

Current To-Do List:
- ~~Blog-wide settings file~~
- ~~Actual template with formatting and whatnot~~
- Pagination (Update: Might add this later, and will likely be a template=implementation)
- ~~Allow arbitrary folders~~
- CSS/JS support
- Template choice support
- Multiple bucket support (Helps with naked domain support)
- Gzip compression support
- Analytics - Some serverside but also Google Analytics support
- RSS Support
- Navigation that makes more sense than sort by date
- "author" page, useful for blogs with multiple authors
- Automatic DNS routing for hosting on domains/sub-domains
- Automatic import of WordPress content
- Intelligent error handling when '<post>.md' doesn't conform to the specified format

<h2>{{postTitle}}</h2>
{{!post}}
%rebase templates/base_template title=postTitle + " - " + config.get("Settings", "title"), h1Title=config.get("Settings", "title")

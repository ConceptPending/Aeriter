<h2>{{postTitle}}</h2>
<div>
{{!post}}
</div>
%rebase templates/base_template title=postTitle + " - " + config.get("Settings", "title"), h1Title=config.get("Settings", "title")

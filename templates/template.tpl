<div class="span2">
</div>
<div class="span8">
<h2>{{postTitle}}</h2>
{{!post}}
</div>
%rebase templates/base_template title=postTitle + " - " + config.get("Settings", "title"), h1Title=config.get("Settings", "title")

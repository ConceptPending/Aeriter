<div class="span2">
</div>
<div class="span8">
<h2>{{postTitle}}</h2>
<p class="undertitle"><span class="post_date"><em>published on {{date}}</em></span><br><span class="author">by <a href="/author/{{author}}">{{author}}</a></span></p>
<div class="post">
    {{!post}}
</div>
</div>
%rebase templates/base_template title=postTitle + " - " + config.get("Settings", "title"), h1Title=config.get("Settings", "title")

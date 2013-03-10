<div class="span2">
</div>
<div class="span8">
<h1>{{postTitle}}</h1>
<p class="undertitle"><span class="post_date"><em>published on {{date.strftime("%B %d, %Y")}}</em></span><br><span class="author">by <a href="/author/{{author}}">{{author}}</a></span></p>
<div class="post">
    {{!post}}
</div>
</div>
%rebase templates/base_template title=postTitle + " - " + config.get("Settings", "title"), h1Title=config.get("Settings", "title")

<div class="row">
    %for post in postMetaData:
    <div class="span6">
        <h2><a href="{{post[2]}}/">{{post[1]}}</a></h2>
        <div class="listing">
            <p><span class="author">by {{post[4]}}</span><span class="date"><em>{{post[0].strftime("%B %d, %Y")}}</em></span></p>
            <p>{{post[5][:-3]}}<a href="{{post[2]}}/">... [continue reading]</a></p>
        </div>
    </div>
    %end
</div>
%rebase templates/base_template title=config.get("Settings", "title"), h1Title=config.get("Settings", "title")

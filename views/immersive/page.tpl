<div class="row">
    %counteri = 0
    %for post in postMetaData:
    <div class="span6">
        <h2><a href="{{post[2]}}/">{{post[1]}}</a></h2>
        <div class="listing">
            <p><span class="author">by <a href="/author/{{post[4]}}">{{post[4]}}</a></span><span class="date"><em>{{post[0].strftime("%B %d, %Y")}}</em></span></p>
            <p>{{post[5][:-3]}}<a href="{{post[2]}}/">... [continue reading]</a></p>
        </div>
    </div>
    %counteri += 1
    %if not counteri % 2: # You should change the number here to the number of items you want per row. You also need to change the "span" class above if you do so.
    </div>
    <div class="row">
    %end
    %end
</div>
%rebase base_template title=config.get("Settings", "title"), h1Title=config.get("Settings", "title"), description=config.get("Settings", "description")

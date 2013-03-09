<div class="row demo-samples">
    %for post in postMetaData:
    <div class="span6">
        <div class="tile">
            <h2><a href="{{post[2]}}/">{{post[1]}}</a></h2>
            <p><span class="author">{{post[4]}}</span> - <span class="date">{{post[0]}}</span></p>
            <p>{{post[5][:-3]}}<a href="{{post[2]}}/">... [continue reading]</a></p>
        </div>
    </div>
    %end
</div>
%rebase templates/base_template title=config.get("Settings", "title"), h1Title=config.get("Settings", "title")

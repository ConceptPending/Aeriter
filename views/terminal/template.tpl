<div class="span12">
<h1>{{postTitle}}</h1>
<p class="undertitle"><span class="post_date"><em>published on {{date.strftime("%B %d, %Y")}}</em></span><br><span class="author">by <a href="/author/{{author}}">{{author}}</a></span></p>
<div class="post">
    {{!post}}
</div>
    <div id="disqus_thread"></div>
    <script type="text/javascript">
        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
        var disqus_shortname = 'conceptpending'; // required: replace example with your forum shortname

        /* * * DON'T EDIT BELOW THIS LINE * * */
        (function() {
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
</div>
%rebase base_template title=postTitle + " - " + config.get("Settings", "title"), h1Title=config.get("Settings", "title"), description=", ".join(tags)

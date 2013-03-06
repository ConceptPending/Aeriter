<html>
	<head>
		<meta name="description" content="{{"PlaceHolder for meta Description"}}">
		<title>{{"Title Placeholder"}}</title>
	</head>
	<body>
		<h1>{{"Blog Title PlaceHolder"}}</h1>
		%for post in postMetaData:
		<h2><a href="{{post[2]}}/">{{post[1]}}</a></h2>
		<p><span class="author">{{post[4]}}</span> - <span class="date">{{post[0]}}</span></p>
		<p>{{post[5][:-3]}}<a href="{{post[2]}}/">... [continue reading]</a></p>
		%end
	</body>
</html>

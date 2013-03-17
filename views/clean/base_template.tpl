<!DOCTYPE html>
<html>
	<head>
		<title>{{title}}</title>
		<meta name="description" content="{{description}}">
		<link rel="icon" type="image/png" href="/resources/{{config.get("Settings", "favicon")}}">
		<link rel="stylesheet" type="text/css" href="/resources/clean.css">
		<link href='http://fonts.googleapis.com/css?family=Merriweather+Sans' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Open+Sans:800' rel='stylesheet' type='text/css'>
	</head>
	<body>
	<div class="header">
		<div class="headline">
		    <a class="logo" href="/"><h1 class="logo">{{h1Title}}</h1></a>
		    <p class="subtitle">{{config.get("Settings", "subtitle")}}</p></div>
	</div>
	<div class="container">
		%include
	</div>
	</body>
</html>

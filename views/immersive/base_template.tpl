<!DOCTYPE html>
<html>
	<head>
		<title>{{title}}</title>
		<meta name="description" content="{{description}}">
		<link rel="stylesheet" type="text/css" href="http://flat-ui.s3-website-us-east-1.amazonaws.com/css/bootstrap.css">
		<link href='http://fonts.googleapis.com/css?family=Merriweather+Sans' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Open+Sans:800' rel='stylesheet' type='text/css'>
		<style>
		    body {
		        background: url("/resources/cafenero.jpg") no-repeat center center fixed;
		        background-size: cover;
		        -webkit-background-size: cover;
		        -moz-background-size: cover;
		        -o-background-size: cover;
		        color: #62615C;
		    }
		    .container {
		        background-color: rgba(231,243,239,0.65);
		        border-left: solid 1px #73726d;
		        border-right: solid 1px #73726d;
		        border-bottom: solid 1px #73726d;
		    }
			a {
			    text-decoration : none;
			    color : #E24B2C;
			}
			a:hover {
			    text-decoration : none;
			    color : #FF5C3D;
			}
			.demo-headline { padding : 25px 0 25px; }
			p {
			    font-size : large !important;
			    margin-bottom : 25px !important;
			    font-family : "Merriweather Sans", sans-serif;
			}
			.listing {
			    margin-bottom : 10px;
			    margin-left: 11px;
			    padding : 0 5px 0 3px;
			    position : relative;
			}
			h2 { margin-top : 10px; }
			h3 { font-size : 20px; }
			h4 { margin-top : 25px; }
			.date {
			    font-size : small;
			    float: right;
			    color: #95948F;
			}
			.post_date {
			    margin-left : 20px;
			    font-size : small;
			}
			.author {
			    margin-left : 20px;
			    font-size : medium;
			}
			.undertitle {
			    margin-top : -10px;
                font-family: "Flat-UI-Icons-16";
			}
			.span6 {
			    padding: 5px;
			}
			.post {
			    padding-left: 5px;
			    margin-left: 5px;
			}
			.row {
			    margin-bottom : 0;
			}
			.headline {
			    text-align: center;
			    margin: 55px 0 55px 0;
			}
			.logo {
			    font-size: 90px;
			    font-weight: 900;
			    line-height: 100px;
			}
			h1 {
			    font-family: "Open Sans", sans-serif;
			}
		</style>
	</head>
	<body>
	<div class="container">
		<a href="/"><div class="headline"><h1 class="logo">{{h1Title}}</h1></div></a>
		%include
	</div>
	</body>
</html>

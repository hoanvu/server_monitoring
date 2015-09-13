$(document).ready(function(){
	setInterval(function() {
		$("#content").load(location.href + " #content>*","");
	}, 5000)
});
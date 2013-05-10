$(function(){
	
	if("#regist"!=location.hash){
		
		$("#login-panel").show();
		$("#regist-panel").hide();
		
	}else{
		
		$("#login-panel").hide();
		$("#regist-panel").show();
		
	}
	
	$(window).bind('hashchange', function(e) { 
		
		if("#login"==location.hash){
			
			$("#login-panel").fadeIn();
			$("#regist-panel").hide();
			
		}else{
			
			$("#regist-panel").fadeIn();
			$("#login-panel").hide();
			
		}
		
	});
	
});
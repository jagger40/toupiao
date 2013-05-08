$(function(){
	
	// prepare the form when the DOM is ready 
	$(document).ready(function() { 
	    var options = { 
	        beforeSubmit:  showRequest,  // pre-submit callback 
	        success:       showResponse,  // post-submit callback 
	    }; 
	 
	    // bind form using 'ajaxForm' 
	    $('.vote_form').ajaxForm(options); 
	}); 
	 
	// pre-submit callback 
	function showRequest(formData, jqForm, options) { 
	   
	    var queryString = $.param(formData); 
	    
	    return true; 
	} 
	 
	// post-submit callback 
	function showResponse(responseText, statusText, xhr, $form)  { 
	   
		var data = jQuery.parseJSON(responseText);
		var votes = data.vote;
	    $("#bar_"+data.choice).css("width",""+votes+"%");
	    $("#vote_"+data.choice).text(votes+"票");
	   
	    $(".btn_vote").remove();
	   
	} 
	
})
// Main App

$(document).ready(function(){
	// Account - Use AJAX to get the Account Edit form and
    // display it on the page w/out a refresh
    $('#gi-container').delegate('.edit-account','click',function(e){
    	e.preventDefault();
    	$('#gi-container').load($(this).attr('href'));
    });
});
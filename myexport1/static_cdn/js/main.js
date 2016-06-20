var main=function(){

	/*// Element at the same level
	// // ?\update Previous
	// // $('#target').prev().attr('style','color:red');

	// // $('#target').prevAll().attr('style','color:red');
	// // update previous until (but not  including )stop
	// $('#target').prevUntil('.stop').attr('style','color:red')
// update next
// $('#target').next().attr('style','color:green');

// $('#target').nextAll().attr('style','color:green');
// update next until (but not  including )stop
 // $('#target').nextUntil('.stop').attr('style','color:green')

var element=$('#target');
var container=$('#container');
var index=container.children().index(element);
$('#display').text('Index is ' +index);
// get returns a DOM element **NOT** jQuery object
var founElement=container.children().get(index);
//convert to jQuery object
var jQueryObject=$(founElement);
jQueryObject.attr('style','color:red');*/

/*
// use addClass and removeClass

// $('#target').addClass('red');
 $('#target').removeClass('blue');
$('#target').attr('style','color:red');
// read an attribute
var style=$('#target').attr('style');
// alert(style);
// remove an attribute value
$('#target').removeAttr('style'); */
/*
// modify text
// $('#target').text('<ul>Updated</ul>');
// Replave html will use the HTML in the parantheses
// $('#target').html('<ul>Updated</ul>')
*/
// $('#target').click(function(){
// 	//This is click event handler for div element
// 	$('#display').text('Div was clicked');
	 // });

//for every div element

// $('div').click(function(){
// // alert('div was click');
// //  This is the DOM element of the item that raised the event
// //convert to jQuery object
// $(this).text('clicked')

// });
// $('a').text('True')
// $('div[class="demo"]').text('Stop');
$('.rating-circle').click(function(){
// $(this).prevAll().add($(this)).css('background-color','green');
$(this).prevAll().addClass('rating-chosen');
$(this).addClass('rating-chosen');
});
$('.rating-circle').hover(function(){
var a=$(this).prevAll().addClass('rating-hover');
$(this).addClass('rating-hover');
$(this).show('rating-hover')
 // $(this).prevAll().removeClass('rating-chosen');
 // $(this).removeClass('rating-chosen');	
});
$('.rating-circle').mouseout(function(){
$(this).prevAll().removeClass('rating-hover');
$(this).removeClass('rating-hover');
$(this).prevAll().addClass('rating-chosen');
// $(this).addClass('rating-chosen');	
});

}

$(document).ready(main);
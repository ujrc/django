// var main=function()
// {/* Push the body and the nav over by 285px over */
// 	$('.icon-menu').click(function(){
// $('.menu').animate({
// 	left:'0px'},200);
// $('section').animate({
// 	left:'285px'},
// 	200);
// });
// 	/* Then push them back */
// $('.icon-close').click(function(){
// $('.menu').animate({
// 	left:'-285px'},
// 	200);
// $('section').animate({
// 	left:'0px'},
// 	200);
// });
// 	};
// // 	$(document).ready(main);

// function myMenu(){
// 	document.getElementById('myDropdown').classList.toggle('show');
// }
// window.onlclick=function(event){
// 	if(!event.target.matches('.dropbtn')){
// 		var dropdowns=document.getElementByClass('dropdown-content');
// 		for(var i=0; i<dropdowns.length;i++){
// 			var openDropdown=dropdowns[i];
// 		}
// 	}
// }
// var main=function(){
// // $('#myDropdown').click(function(event){
// // $('.dropbtn')
// // });
// $( ".selector" ).menu({
//   icons: { submenu: "ui-icon-circle-triangle-e" }
// });
// }
// $(document).ready(main);
 
 var main=function(){

$('#nav li').hover(function(){
$('ul',this).slideDown();
// $('a',this).css({'background':'transparent','color':'#1BBC9C'});
},function(){
$('ul',this).hide();
// $('a',this).css({'background':'blue','color':'white'});
});
 }
 $(document).ready(main);


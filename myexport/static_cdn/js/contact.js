var main=function(){
$('#submit').click(function(){
	var name=$('#name').val();
	var emai=$('#email').val();
	var subject=$('#subject').val();
	var content=$('#content').val();
$('#message').empty();

if (name=='' || email=='' || content=='')
{
	alert('Required');
}
else
{
$.post('')
}
});

}

$(document).ready(main);

var myLocation=new google.maps.LatLng(43.074872,-89.381350);

function initialize(){
	var mapProperties={
		center: myLocation,
		zoom:10,

		mapTypeControl:true,
		mapTypeControlOptions:
		{
		style:google.maps.MapTypeControlStyle.DROPDOWN_MENU,
		position:google.maps.ControlPosition.TOP_CENTER
		},

		mapTypeId:google.maps.MapTypeId.ROADMAP
	};
	var myMap=new google.maps.Map(document.getElementById("gmap"),mapProperties);
	var marker=new google.maps.Marker({
	position:myLocation,
	// animation:google.maps.Animation.BOUNCE,
	title:'click to zoom',
	
}); 
marker.setMap(myMap);

// Zoom to 9 when clicking on marker

// google.maps.event.addDomListener(marker,'click',function(){
// 	myMap.setZoom(10);
// 	myMap.setCenter(marker.getPosition());
// });

var infoWindow=new google.maps.InfoWindow({content:'EXPORT ABROAD, INC.'});
infoWindow.open(myMap,marker);
}
google.maps.event.addDomListener(window,'load',initialize);

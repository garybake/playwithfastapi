
$(document).ready(function() {
    var url = '/api/v1/locations/key';
    $.get(url, function( data ) {
        if(data.hasOwnProperty('key')){
            drawMap(data.key);
        } else {
            alert('maps access key missing')
        }
    });
});

function drawMap(accessToken) {

    var mymap = L.map('mapid').setView([51.505, -0.09], 13);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: accessToken
    }).addTo(mymap);
}
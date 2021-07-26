
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
    var myMap = initialiseMap(accessToken);
    addMarker(myMap, 51.5, -0.09);
    addCircle(myMap, 51.508, -0.11);
    var polyMatrix = [
        [51.509, -0.08],
        [51.503, -0.06],
        [51.51, -0.047]
    ]
    addPolygon(myMap, polyMatrix);
    addRoute(myMap);
}

function initialiseMap(accessToken) {

    var myMap = L.map('mapid').setView([51.505, -0.09], 13);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: accessToken
    }).addTo(myMap);

    return myMap
}

function addMarker(myMap, lat, lng) {
    var marker = L.marker([lat, lng]).addTo(myMap);
}

function addCircle(myMap, lat, lng, radius=500) {
    var circle = L.circle([lat, lng], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: radius
    }).addTo(myMap);
}

function addPolygon(myMap, polyMatrix) {
    var polygon = L.polygon(polyMatrix).addTo(myMap);
}

function addRoute(myMap){
    //https://github.com/skedgo/tripkit-leaflet
}


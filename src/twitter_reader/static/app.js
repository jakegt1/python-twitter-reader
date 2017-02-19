createMarkerObject = function(coords){
    return {
        lng: coords[0],
        lat: coords[1],
        title: "Tweet Location"
    }
}
createMarkers = function(map, coords){
    for(let coord of coords){
        map.addMarker(createMarkerObject(coord));
    }
}
$('.tweet-text').click(function(){
    var $this = $(this);
    var $url = $this.find('#tweet-url');
    window.location.href = $url.text();
})
$('.tweet-header').click(function(){
    var id = this.id;
    window.location.href = "/#"+id;
})
$( document ).ready(function() {
    var firstCoord = null;
    var coordsList = [];
    $('.tweet-text').find('#tweet-place').each(function(index, element){
        var coords = JSON.parse(element.textContent);
        if(!firstCoord){
            firstCoord = coords
        }
        coordsList.push(coords);
    });
    if(!firstCoord){
        firstCoord = [-2.3599, 51.3758];
    }
    window.map = new mapTools({
        id: 'map',
        lat: firstCoord[1],
        lng: firstCoord[0]
    }, function (err, map) {
        if (!err) {
            createMarkers(map, coordsList)
        }
    });
});


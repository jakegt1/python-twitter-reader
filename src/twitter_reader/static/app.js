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
    var map = new mapTools({
        id: 'map',
        lat: 41.3833,
        lng: 2.1833
    }, function (err, map) {
        if (!err) {
            console.log('Map Loaded!', map.instance);
        }
    });
});


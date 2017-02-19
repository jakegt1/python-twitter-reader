$('.tweet-text').click(function(){
    var $this = $(this);
    var $url = $this.find('#tweet-url');
    window.location.href = $url.text();
})
$('.tweet-header').click(function(){
    var id = this.id;
    window.location.href = "/#"+id;
})

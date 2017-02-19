$('.tweet-text').click(function(){
    $this = $(this);
    $url = $this.find('#tweet-url');
    window.location.href = $url.text();
})

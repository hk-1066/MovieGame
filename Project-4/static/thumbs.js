$(window).on('load', function() {
    console.log('the page is loaded');
});
$('.widget.thumbs-up').on('click', function() {
    
    var elt = $(this);
    console.log("csrf = " + csrfToken)
    $.ajax('/api/update_thumbs_up', {
        method: 'POST',
        data: {
            //ToDo: add data
            _csrf_token: csrfToken
        },
        success: function(data) {
            /* called when post succeeds */
            console.log('post succeeded with result %s', data.result);
        },
        error: function() {
            /* called when post fails */
            console.log('post failed');
        }
    });
});


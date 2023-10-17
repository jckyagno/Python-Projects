$(document).ready(function () {
    let panel = $('.item_panel');

    if (panel != null) {
        panel.fadeOut(0).fadeIn(500);
    }

    // Back to top button. \\
    var topButton = document.getElementsByClassName("top")[0];
    $(window).scroll(function () {
        if ($(window).scrollTop() > 300) {
            $(topButton).addClass('show');
        } else {
            $(topButton).removeClass('show');
        }
    });

    $(topButton).on('click', function (e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: 0 }, '300');
    });
});

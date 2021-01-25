// js specific for article detail page

// from: https://css-tricks.com/snippets/jquery/shuffle-dom-elements/
(function ($) {
    $.fn.shuffle = function () {
        var allElems = this.get(),
            getRandom = function (max) {
                return Math.floor(Math.random() * max);
            },
            shuffled = $.map(allElems, function () {
                var random = getRandom(allElems.length);
                // Use of clone means we break references. But it's fine for this example.
                var randEl = $(allElems[random]).clone(true)[0];
                allElems.splice(random, 1);
                return randEl;
            });

        this.each(function (i) {
            $(this).replaceWith($(shuffled[i]));
        });

        return $(shuffled);
    };

})(jQuery);

(function () {
    jQuery("#quotes-shuffler").on('click', function (e) {
        e.preventDefault();
        jQuery(".ticker-row").shuffle();
    })
})();
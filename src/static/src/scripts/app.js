'use strict';
/*global $:false */


$(document).ready(function(){

    // Add class to body when navigation is expanded
    var $body = $('body');
    var $menuTrigger = $('.menu__gutter__trigger');

    $menuTrigger.click(function(){
        $body.toggleClass('menu--expanded');
        return false;
    });

    // Toggle sidebar/column
    var $columnTrigger = $('.sidebar__trigger, .header__trigger');
    $columnTrigger.click(function(){
        $body.toggleClass('column--expanded');
        return false;
    });

    // Equalize the heights of selected columns.
    var equalizeColumns = function() {
        $('[data-equal-columns]').each(function(i, row){
            var $row = $(row);
            var $columns = $row.find('[data-column]');
            $columns.css('height','auto').height('auto');

            if($(window).width() > 800) {
                var max = 0;
                $columns.each(function(j, column){
                    var $column = $(column);
                    var height = $column.outerHeight();
                    max = (height > max)? height : max;
                });

                $columns.each(function(j, column){
                    var $column = $(column);
                    var padding = $column.innerHeight() - $column.height();
                    var height = max - padding;
                    $column.animate({
                        height: height
                    }, 250).height(height);
                });
            }
        });
    };
    // Run equalize on first load as well as when a resize event stops
    if ($('[data-equal-columns]').length > 0) {
        var timer;
        $(window).on('load', function(){
            equalizeColumns();
        }).on('resize', function() {
            clearTimeout(timer);
            timer = setTimeout(equalizeColumns, 400);
        });
    }
});

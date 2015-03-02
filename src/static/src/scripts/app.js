'use strict';
/*global $:false */


$(document).ready(function(){
    var $body = $('body');


    // Toggle sidebar/column
    var setupSidebarToggle = function(){
        var $columnTrigger = $('.sidebar__trigger, .header__trigger');
        $columnTrigger.click(function(){
            $body.toggleClass('column--expanded');
            return false;
        });
    };

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

    // Setup seamless ajax navigation
    var $menuLinks = $('.menu__nav li a');
    var $menuTrigger = $('.menu__gutter__trigger');
    var $container = $('.page-wrapper');

    // Fetch the content of the page via ajax and insert it in the current page
    var getPageContent = function(href) {
        console.log('Getting ' + href);
        $.get(href, function (data) {
            $container.fadeOut(150, function(){
                $container.html(data.content);

                var $content = $container.find('[data-seamless-nav]');
                var metaTitle = $content.attr('data-meta-title');
                var metaDescription = $content.attr('data-meta-description');

                document.title = metaTitle;
                $('meta[name=description]').attr('content', metaDescription);

                history.pushState({}, null, href);
                $container.fadeIn(150);
                $(window).trigger('load');
            });
        });
    };

    // When an anchor link is clicked
    var setupSeamlessNavigationLinks = function() {
        $('a').off('click').click(function(e){
            var $this = $(this);
            var href = $this.attr('href');
            var isAbsURL = new RegExp('^(?:[a-z]+:)?//', 'i');
            if(!isAbsURL.test(href)) {
                e.preventDefault();
                getPageContent(href);
                return false;
            }
        });
    };

    // When the back button is clicked
    window.onpopstate = function (e) {
        var href = window.location.href;
        e.preventDefault();
        getPageContent(href);
        $(window).trigger('load');
    };

    // When the menu links are clicked
    $menuLinks.click(function(){
        $menuLinks.parent('li').removeClass('active');
        $(this).parent('li').addClass('active');
        return false;
    });

    // Add class to body when navigation is expanded
    $menuTrigger.click(function(){
        $body.toggleClass('menu--expanded');
        return false;
    });

    $(window).on('load', function(){
        setupSidebarToggle();
        equalizeColumns();
        setupSeamlessNavigationLinks();
    });

    var timer;
    $(window).on('resize', function(){
        clearTimeout(timer);
        timer = setTimeout(equalizeColumns, 400);
    });
});

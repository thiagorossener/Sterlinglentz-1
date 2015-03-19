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

    // Equalize the heights of columns marked with [data-equal-columns]
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
    var timer;
    $(window).on('resize', function(){
        clearTimeout(timer);
        timer = setTimeout(equalizeColumns, 400);
    });

    // Add class to body when navigation is expanded
    var $menuTrigger = $('.menu__gutter__trigger, .menu__mobilegutter__trigger');
    $menuTrigger.click(function(){
        $body.toggleClass('menu--expanded');
        return false;
    });

    // Add class to body when sidebar
    var $sidebarTrigger = $('.menu__mobilesidebar__trigger');
    $sidebarTrigger.click(function(){
        $body.toggleClass('sidebar--expanded');
        return false;
    });

    // When the menu links are clicked
    var $menuLinks = $('.menu__nav li');
    var $menuLogo = $('.menu__logo');
    $menuLinks.click(function(){
        // Active/deactivate menu links
        $menuLinks.removeClass('active');
        $(this).addClass('active');

        // Fade in the feral logo in menu
        setInterval(function(){
            $menuLogo.css('opacity', 1);
        }, 2000);
    });

    // Close the nav if below < 1100px
    $(window).on('resize', function(){
        if($(window).width() > 1100) {
            $body.removeClass('menu--expanded');
        }
    });

    /*
     * Dynamic loading of pages ("seamless navigation")
     * All of our internal pages are loaded asyncrously to give a "seamless
     * navigation" experience.
     */

    // Fetch the content of the page via ajax and insert it in the current page
    var $container = $('.page-wrapper');
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
                $container.fadeIn(150, function(){
                    $('html, body').animate({ scrollTop: 0 }, 250);
                });
                $(window).trigger('load');
            });
        });
    };

    // When the back button is clicked, unload the previous page
    window.onpopstate = function (e) {
        var href = window.location.href;
        e.preventDefault();
        getPageContent(href);
        $(window).trigger('load');
    };

    // When an link is clicked, dynamically load the content if it's a local page
    var setupSeamlessNavigationLinks = function() {
        $('a').off('click').click(function(e){
            var $this = $(this);
            var href = $this.attr('href');
            var isAbsURL = new RegExp('^(?:[a-z]+:)?//', 'i');
            if(!isAbsURL.test(href)) {
                getPageContent(href);
                e.preventDefault(); // Important to stop page redirection
            }
        });
    };

    // When a load occurs (either the initial load or a subsequent dynamic
    // load), rerun javascript relevant to the content of the page
    $(window).on('load', function(){
        setupSidebarToggle();
        equalizeColumns();
        setupSeamlessNavigationLinks();
    });
});

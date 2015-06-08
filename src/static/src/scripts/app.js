var controllers = {
    utils: {
        getArgs: function($element) {
            try {
                return eval("(" + $element.attr("js-controller-args") + ")") || {};
            } catch(ex) {
                return {};
            }
        }
    },
    get : function(selector) {
        return $(selector).data("js-controller");
    }
};

var bindJSControllers = function() {
    $("[js-controller]").each(function() {
        var $element = $(this);
        if (!$element.data('js-controller-loaded')) {
            var handler = $(this).attr('js-controller');
            var options = controllers.utils.getArgs($element);
            var api = new controllers[handler]($element, options);
            $element.data('js-controller-loaded', true);
            $element.data('js-controller', api);
            console.log("Loaded controller '" + handler + "'");
        } else {
            console.log("! Controller '" + handler + "' is already loaded");
        }
    });
};

controllers.tooltip = function($element, options) {
    var content = $element.attr("js-tooltip-content");
    $element.tooltipster({
        content: content,
        position: "right",
        theme: "tooltipster-sterling",
        contentAsHTML: true,
        delay: 100,
        maxWidth: 170,
        interactive: true,
        speed: 100
    });
}

controllers.fsImage = function($element, options) {
    var api = {};
    var defaults = {};
    var settings = $.extend( {}, defaults, options);

    // Search the page for all images and create map
    var images = {};
    var $images = $("[js-fsimage]");
    $images.each(function(i, el){
        images[$(el).attr("js-fsimage")] = $(el);
    });

    var $close = $("[js-fsimage-close]");
    var $img = $("[js-fsimage-img]");

    api.show = function() {
        $element.fadeIn("fast");
    };

    api.hide = function() {
        $element.fadeOut("fast");
    };

    api.loadImage = function(src) {
        $img.attr("src", src);
    }

    $close.click(function(){
        api.hide();
    });

    $images.click(function(){
        api.loadImage($(this).attr("js-fsimage"));
        api.show();
    })

    return api;
}

$(function() {
    bindJSControllers();
});





// Older Javascript (move to above controller approach)
$(document).ready(function(){
    var $body = $('body');

    // Setup the frontpage fullpage widget
    var setupFrontpageFullpage = function() {

        try {
            $.fn.fullpage.destroy('all');
        } catch (err) {

        }

        var $fullpage = $(".fullpage");
        if ($fullpage.length > 0) {
            var $sections = $(".fullpage__section");

            $fullpage.fullpage({
                sectionSelector: '.fullpage__section',
                verticalCentered: false,
                afterRender: function(){
                    // Fade the whole element in on initial load
                    $fullpage.css("opacity", 1);
                }
            });

            $(".fullpage__arrow--down").click(function(){
                $.fn.fullpage.moveSectionDown();
            });

            $(".fullpage__arrow--up").click(function(){
                $.fn.fullpage.moveSectionUp();
            });
        }
    };

    // Setup the sidebar toggles
    var setupSidebarToggle = function(){
        var $columnTrigger = $('.sidebar__trigger, .header__trigger');
        $columnTrigger.off('click').click(function(){
            $body.toggleClass('sidebar--expanded');
            return false;
        });

        // If there is a sidebar on the page, show the menu navigation sidebar
        // toggle, otherwise hide it
        var $mobileSidebarTrigger = $('.menu--mobile .sidebar__trigger');
        var $mobileTitle = $('.menu__title--mobile');
        if($('[data-show-sidebar-trigger]').length > 0) {
            $mobileSidebarTrigger.show();
            $mobileTitle.css("right", "7rem");
        } else {
            $mobileSidebarTrigger.hide();
        }
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

    // Expand/contract the menu when a menu trigger button is clicked. On desktop
    // the menu is open by default (using an extra css class on the body element)
    var $menuTrigger = $('.menu__trigger');
    $menuTrigger.click(function(){
        if($body.hasClass('menu--expanded--onload')){
            $body.removeClass('menu--expanded--onload');
        } else {
            $body.toggleClass('menu--expanded');
        }
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

        // Close the menu on click of menu link when in mobile
        if($(window).width() < 800){
            $body.removeClass('menu--expanded');
            $body.removeClass('menu--expanded--onload');
        }
    });

    // Close the nav if we resize below < 1100px
    $(window).on('resize', function(){
        if($(window).width() < 1100) {
            $body.removeClass('menu--expanded');
            $body.removeClass('menu--expanded--onload');
        }
    });

    /*
     * Dynamic loading of pages ("seamless navigation")
     * All of our internal pages are loaded asyncrously to give a "seamless
     * navigation" experience.
     */
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
        setupFrontpageFullpage();
    });
});

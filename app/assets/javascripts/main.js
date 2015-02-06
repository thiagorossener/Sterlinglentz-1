(function($){

    if ($.browser.mobile) {
        $('body').addClass('is-mobile').removeClass('navbar-expanded');
    }

    function setupSeamlessNav() {

        function swapContent(href, after) {
            var siloSelector = '.window-wrapper';
            var containerSelector = '.page-wrapper';
            var $silo = $(siloSelector);
            var $container = $(containerSelector);
            var title = $('a.x-silo[href="' + href + '"]').text();
            $container.addClass('x-silo-change');
            $.get(href, function (data) {
                var $got = $(data);
                $container.html($got.find('.page-wrapper').html()).removeClass('x-silo-change')
                $silo.attr('class', $got.find('.window-wrapper').attr('class'));
                console.log(title);
                if (title !== 'Index' && title !== 'JDSLabs') {
                    $('.nav-silo-name').text(title.toUpperCase());
                }
                else
                {
                    $('.nav-silo-name').text("");
                }
                window.scrollTo(0,0);
                setTimeout(after, 10);
            });
        }

        $('a.x-silo').click(function (e) {
            var href = $(this).attr('href');
            swapContent(href, function (data) {
                setupPage();
                $('body').removeClass('navbar-expanded');
                history.pushState({}, null, href);
            });
            return false;
        });

        // when clicking back button
        window.onpopstate = function (e) {
            var state = window.event.state;
            var w = $(window).width();
            var href = window.location.href;

            e.preventDefault();
            swapContent(href, setupPage);
        }
    }

    function setupGeneralParallax() {
        $('.image-strip.parallax').each(function (i, el) {
            $(el).attr('data-initial-height', $(el).height());
        });

        var onScroll = function (e) {
            var yPos = $(this).scrollTop();
            $('[data-parallax-ratio]').each(function (i, el) {
                var speed = parseFloat($(el).attr('data-parallax-ratio')) - 1;
                var top = parseFloat($(el).attr('data-initial-top')) + yPos * speed;
                $(el).css({
                    'top': top
                });
            });
            $('.image-strip.parallax').each(function (i, el) {
                var height0 = $(el).data('initial-height');
                var yPosPlus = Math.max(0, yPos);
                if (yPosPlus < height0) {
                    $(el).css({
                        'margin-top': +yPosPlus * 5 / 8,
                        height: height0 - yPosPlus,
                    });
                }
            });
        };

        var scrollable = window;
        $(scrollable).scroll(onScroll);
        onScroll.apply(scrollable);
    }

    function setupWorkParallax() {
        var $projects = $('.work-project');
        var $leftProjects = $('.work-project:nth-child(odd)');
        var $rightProjects = $('.work-project:nth-child(even)');

        function setPositions() {
            var totalHeight = 0;

            $projects.css({
                position: 'absolute',
                // margin: 0,
            });

            $('.work-project').each(function (i, el) {
                var $el = $(el);
                var yOffset = $el.height() * 0.707;
                var top = totalHeight;
                var speed;
                $el.attr('data-initial-top', top);
                $el.attr('data-parallax-ratio', 1 - parseFloat(i) / 10);
                $el.css({
                    top: top,
                    left: 0,
                });
                totalHeight += yOffset;
            });

            $('.work-foot').css({
                top: totalHeight + 40
            })

            $('.work-bunnies .bunny').each(function (i, el) {
                var $el = $(el);
                var top = $el.position().top;
                $el.attr('data-initial-top', top);
                $el.attr('data-parallax-ratio', 1.7);
            });
        }

        var onScroll = function (e) {
            var yPos = $(this).scrollTop();
            var yCheck = yPos + $(window).height() / 2;
//            var yLimit = $('.work-foot').position().top;
            // var yLimit = $('.work-project:last-child').position().top + $('.work-project:last-child').height()/2;
            // if(yCheck > yLimit) {
            // 	// window.scroll(0, 0);
            // 	// yPos = yLimit - $(window).height();
            // 	return;
            // }
            // else {
            // 	console.log(yCheck, yLimit);

            // }
            $('[data-parallax-ratio]').each(function (i, el) {
                var speed = parseFloat($(el).attr('data-parallax-ratio')) - 1;
                var top = parseFloat($(el).attr('data-initial-top')) + yPos * speed;
                // console.log(i, top);
                $(el).css({
                    'top': top
                });
            });
        };

        var scrollable = '.window-wrapper';
        $(scrollable).scroll(onScroll);
        onScroll.apply(scrollable);

        setPositions();
    }


    function setupPage() {
        if (!$.browser.mobile) {
            setupGeneralParallax();
            setupWorkParallax();
        }
    }

    $(function () {

        setupSeamlessNav();
        setTimeout(setupPage, 100);

        //horizontal
        $('.nav-expand-button').click(function () {
            $('body').toggleClass('navbar-expanded');
        })

        $('.blog-page-mark').click(function () {
            $('body').toggleClass('blog-bar-expanded');
        })

        $('.nav-links a').click(function (e) {

        })

    });

})(jQuery);
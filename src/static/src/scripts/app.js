'use strict';
/*global $:false */


$(document).ready(function(){
    var $body = $('body');
    //var $menu = $('.menu');
    var $menuTrigger = $('.menu__gutter__trigger');
    //var $menuDrawer = $('.menu__drawer');

    $menuTrigger.click(function(){
        $body.toggleClass('menu--expanded');
    });
});

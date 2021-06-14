// For Plone 4 implement a fake require/define that operates synchronously
if (window.define === undefined) {
    window.define = function (name, requirements, callable) {
        callable();
    };
    window.require = function(requirements, callable) {
        callable();
    };
}

define('jazkarta-tesserae', [
  'jquery',
], function($) {
    if ($ === undefined) {
        $ = window.jQuery;
    }
    $(function() {
        $('.item.active').find(".to-animate").addClass('fadeInUp animated');
        $('.carousel').on('slid.bs.carousel', function () {
            $('.item.active').find(".to-animate").addClass('fadeInUp animated');
        });
        $('.carousel').on('slide.bs.carousel', function () {
            $('.item.active').find(".to-animate").addClass('fadeInUp animated');
        });
    });
});

define('jazkarta-tesserae', [
  'jquery',
], function($) {
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

$(function () {
    $('.up').on('click', function () {
        var wrapper = $(this).closest('.accordion_wrap');
        wrapper.insertBefore(wrapper.prev());
    });
    $('.down').on('click', function () {
        var wrapper = $(this).closest('.accordion_wrap');
        wrapper.insertAfter(wrapper.next());
    });
});

$(".accordion_header").on('click', function(e){
    var panel = $(this).parent().siblings('.accordion_body');
    if (e.target.className != "down" && e.target.className != "up"){
        panel.toggle();
    }
})
// feather
if (typeof feather !== "undefined") {
    feather.replace();
}
// cases
$('.cases__item > div').click(function() {
    $(this).children('.cases__item__back').show();
});
$('.cases__item__back .close').click(function(e){
    e.stopPropagation();
    $(this).parent().hide();
});
// modal
$('#contact__request').click(function() {
    $('.contact').show();
});
$('.contact .close').click(function(){
    $('.contact').hide();
});
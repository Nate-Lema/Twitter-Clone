$(function(){
    // excuted when js-menu-icon clicked
    $('.js-menu-icon').click(function(){
        // $(this) :self element ,namely div.js-menu-icon
        // name() next to div.js-menu-icon namely div.name
        // toggle() switch show and hide the menu icon
        $(this).next().toggle();
    })
})
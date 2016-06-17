/**
 * Created by harri on 6/6/2016.
 */

// $(window).on("load", function() {
//     console.log('window load')
//     $("#createUser").hide()
// });

$("#newUser").click(function(){
    console.log('newUser clicked')
    newUser();
});

function newUser() {
    console.log('inside newUser1')
    $("#createUser").removeClass("no-show");
    $("#login").removeClass("show");
    
    $("#createUser").addClass("show");
    $("#login").addClass("no-show");
    // $("#createUser").attr("class", "show"); //works
    // $("#createUser").show() //works
    // $("#login").hide() //works
    console.log('inside newUser2')
}
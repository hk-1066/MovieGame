/**
 * Created by harri on 6/7/2016.
 */

var a = io.connect('http://' + document.domain + ':' + location.port);


$(".movieSearch").click(function(){
    console.log('inside movieSearch click');
    getMovie();
});

function getMovie() {
    console.log('inside getMovie');
    a.emit("getMovie", {movie_title: "galaxy quest"});
};
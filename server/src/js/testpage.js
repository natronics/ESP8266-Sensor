require("../style.sass");
var $ = require('jquery');

$(document).ready(function() {

    $("#testdata").submit(function(event) {
        event.preventDefault();

        // Send the data using post
        var posting = $.post('/push/', {sensor: $('#sensor').val()});

        // Result:
        posting.done(function(data) {
            console.log(data);
        });
        posting.fail(function(data) {
            console.log("Failure!");
        });
    });
});

require("../style.sass");
var $ = require('jquery');

$(document).ready(function() {

    var jqxhr = $.getJSON( "/data/", function() {})
        .done(function(data) {
            for (var i in data.data) {
                var line = data.data[i];
                $("#datatable").append("<tr><td>" + line.time + "</td><td>" + line.value + "</td></tr>");
            }
        });
});

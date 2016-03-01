var $ = require('jquery');

$(document).ready(function() {
    $("#testBtn").click(function() {
        $.post( "/push/", {'key': "Value"}, function() {
            
        });
    }); 
});

require("../style.sass");
var $ = require('jquery');
var dateFormat = require('dateformat');

var sensor_def = {
  input_voltage: 3.3,
  resolution: 1023,
  rate: 0.01,
  conversion: -273.15,
  bias: -5.4
}

$(document).ready(function() {

    var jqxhr = $.getJSON( "/data/", function() {})
        .done(function(data) {
            for (var i in data.data) {
                var line = data.data[i];

                var date = new Date(line.time*1000);

                var raw_temp = line.value;
                var temp = ((sensor_def.input_voltage / (sensor_def.resolution / raw_temp)) / (sensor_def.rate)) + sensor_def.conversion - sensor_def.bias;
                $("#datatable").append('<tr><td class="data time">' + dateFormat(date, "yyyy-mm-dd HH:MM:ss Z", true) + '</td><td class="data raw">' + raw_temp + '</td><td class="data temp">' + temp.toFixed(2) + '</td></tr>');
            }
        });
});

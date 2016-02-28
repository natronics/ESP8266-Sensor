# Arduino Code For ESP8266

Firmware for the ESP8266 chip using the Arduino platform. Requires the [ESP8266 Arduino addon](https://github.com/esp8266/Arduino).
See [these instructions for installing in your Ardunio environment](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide/installing-the-esp8266-arduino-addon).


## Install

Copy this directory to your `Sketches` folder, and rename to "`ESP8266_Sensor`" or, even better, use a simlink:

    $ ln -s path_to_this_folder path_to_sketches/ESP8266_Sensor


### Edit Environment Details

Make a copy of the file `environment.h.dist` called `environment.h` and edit it, filling out the WiFi connection details and the name or IP Address of the place you'll be pushing code to (where the server part of this project is deployed)

Now you can build and flash the ESP8266

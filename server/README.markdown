# ESP8266 Sensor Web Server

[![Build Status](https://travis-ci.org/natronics/ESP8266-Sensor.svg?branch=master)](https://travis-ci.org/natronics/ESP8266-Sensor)


This acts both as a place to push data from the ESP8266 and a display for the data.



## Install

We need python and pip (for the webserver) and nodejs and npm (for building all the assets and bundling them including external packages into the page).

It's usually best to work inside a virtual environment for python, and then you wont need sudo and you wont mess up any other python projects you might be using. Node will take care of this for us by only installing locally by default.

### Python Dependencies

    $ pip install -r requirements.txt

### Node Dependencies

    $ npm install

### Build Site

    $ make pack



## Run The Server

    $ make demo

# ssh login to your server, e.g. username@servername
SERVER=lapis

# bare repo locaion
BARE_GIT=~/ESP8266-Sensor.git


sync:
	scp $(SERVER):$(BARE_GIT)/hooks/post-receive ./
	scp $(SERVER):/etc/supervisor/conf.d/80.ESP8266-Sensor.conf ./
	scp $(SERVER):/etc/nginx/sites-available/esp8266.conf ./

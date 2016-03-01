all: demo

demo: pack
	python esp_server.py

lint:
	flake8 esp_server.py
	flake8 esp_server_test.py

pack:
	./node_modules/.bin/webpack --bail

test: pack lint
	python esp_server_test.py

clean:
	rm -f static/*.js
	rm -f *.pyc

cleandata:
	rm -f data/*.json

all: demo

demo:
	python esp_server.py

lint:
	flake8 esp_server.py
	flake8 esp_server_test.py

test: lint
	python esp_server_test.py

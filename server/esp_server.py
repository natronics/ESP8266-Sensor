from flask import Flask, render_template, request, url_for
from tinydb import TinyDB
import time
import json

app = Flask(__name__)
db = TinyDB('./data/database.json')
sensor_data = db.table('sensor')


@app.route("/")
def index():
    return render_template('home.html', page_resources=[url_for('static', filename='index.js')])


@app.route("/test/")
def test():
    return render_template('test.html', page_resources=[url_for('static', filename='testpage.js')])


@app.route("/push/", methods=['POST'])
def push():
    data = request.form
    sensor_value = data.get('sensor', None)
    if sensor_value:
        sensor_data.insert({'time': float(time.time()), 'value': sensor_value})
    return json.dumps({'message': "success"}), 200


@app.route("/data/")
def get():
    data = sensor_data.all()
    return json.dumps({'message': "success", 'data': data}), 200


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

from flask import Flask, render_template, request, url_for
from tinydb import TinyDB
import time
import subprocess
import json

app = Flask(__name__)
db = TinyDB('./data/database.json')
sensor_data = db.table('sensor')
gitversion = "?unknown?"
runon = "?unknown?"
try:
    p = subprocess.Popen(["git", "describe", "--tags", "--always"], stdout=subprocess.PIPE)
    gitversion = p.communicate()[0]
except EnvironmentError:
    print "unable to run git, unknown version"
try:
    p = subprocess.Popen(["uname", "-a"], stdout=subprocess.PIPE)
    runon = p.communicate()[0]
except EnvironmentError:
    print "unknown server"


@app.route("/")
def index():
    options = {
        'page_resources': [url_for('static', filename='index.js')],
        'pagetitle': "ESP8266 Sensor",
        'version': gitversion,
        'server': runon,
    }
    return render_template('home.html', **options)


@app.route("/test/")
def test():
    options = {
        'page_resources': [url_for('static', filename='testpage.js')],
        'pagetitle': "Load Test Data",
        'version': gitversion,
        'server': runon,
    }
    return render_template('test.html', **options)


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

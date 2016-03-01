from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('base.html')


@app.route("/test/")
def test():
    return render_template('test.html')


@app.route("/push/", methods=['POST'])
def push():
    data = request.form
    print data
    return json.dumps({'message': "success"}), 200


if __name__ == "__main__":
    app.run()


# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!222222222222222222'

@app.route('/keyboard')
def keyboard():

    ret = {
  "type" : "buttons",
  "buttons" : ["선택 1", "선택 2", "선택 3"]
}

    return ret



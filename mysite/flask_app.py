# _*_ coding: utf-8 _*_
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!222222222222222222'

@app.route('/keyboard')
def keyboard():
    keyboard = {"type" : "buttons",  "buttons" : ["선택 1", "선택 2", "선택 3"]}
    return keyboard
@app.route('/message')
def messauge():
    return

if __name__ == '__main__':
    app.debug = True


app.run()
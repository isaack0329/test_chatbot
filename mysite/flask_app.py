# -*- coding: utf-8 -*-
import os
from flask import Flask,request, jsonify
import sqlalchemy

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/yacha')
def WelcomeToMyapp():
    return 'Welcome ! '

@app.route('/keyboard')
def Keyboard():
    keyList= ["temperature","sensor"]
    keyboardList = {'type': 'buttons', 'buttons': keyList}
    return jsonify(keyboardList)

@app.route('/message', methods=['POST'])
def GetMessage():
    content = request.get_json()
    print(content)
    text = content['content']
    textContent = {"text":text}
    textMessage = {"message":textContent}
    return jsonify(textMessage)

@app.route('/freinds')





@app.errorhandler(404)
def page_not_found(e):
    text = "Invalid command!"
    textContent = {"text":text}
    errorMessage = {"message":textContent}
    return jsonify(errorMessage)

#port = os.getenv('PORT', '5000')
#if __name__ == "__main__":
#	app.run(host='0.0.0.0', port=int(port))
from flask import Flask

app = Flask(__name__)

@app.route("/") 

def hello_world():

    file = open('keyboard.txt','r')
    temp = file.read()
    file.close
    return temp
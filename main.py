from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_wrld():
    return "<b>Hello Wrld</b>"
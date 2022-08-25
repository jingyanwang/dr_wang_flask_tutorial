from markupsafe import escape

from flask import Flask

app = Flask(
    __name__
    )

@app.route("/")

def index():
	return "Index page"


@app.route("/hello")

def hello(
	):
	return "Hello, world"

'''
flask --app routing --debug run --host=0.0.0.0 

http://10.94.245.169:5000/hello
'''
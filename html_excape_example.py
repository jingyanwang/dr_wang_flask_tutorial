from markupsafe import escape

from flask import Flask

app = Flask(
    __name__
    )


@app.route("/<name>")

def hello(
	name,
	):
	return f"hello, {name}!"

'''
flask --app html_excape_example --debug run --host=0.0.0.0 

http://10.94.245.169:5000/jingyan
'''
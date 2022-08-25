from flask import render_template

from flask import request

from flask import url_for

from markupsafe import escape

from flask import Flask

app = Flask(
    __name__
    )


@app.route('/hello/')
@app.route('/hello/<name>')

def hello(
	name = None
	):
	return render_template(
		"hello.html",
		name = name,
		)


'''

flask --app rendering_templates --debug run --host=0.0.0.0 


http://10.94.245.169:5000/hello/

http://10.94.245.169:5000/hello/jingyan


'''
from flask import render_template

from flask import request

from flask import url_for

from markupsafe import escape

from flask import Flask

app = Flask(
    __name__
    )


@app.route(
	'/login',
	methods = [
		'POST',
		'GET',
		])

def login():
	if request.method == 'POST':
		return render_template(
			"login.html",
			username = request.form('username'),
			password = request.form('password'),
			)
	else:
		return render_template(
			"login.html")


'''

flask --app the_request_object --debug run --host=0.0.0.0 


http://10.94.245.169:5000/login

curl -X POST http://10.94.245.169:5000/login

'''
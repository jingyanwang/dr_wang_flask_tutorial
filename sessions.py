from flask import render_template

from flask import request

from flask import url_for

from markupsafe import escape

from flask import Flask

from flask import make_response

from flask import abort, redirect, url_for

from flask import session



app = Flask(
    __name__
    )
app.secret_key = "JDGKDNGKDGyOGDI"


@app.route("/index")

def index():
	if "username" in session:
		return f'Loggin as {session["username"]}'
	return "You are not loggedin"


@app.route('/login', 
	methods = [
		'GET',
		'POST',
		])

def login():
	if request.method == 'POST':
		session["username"] = request.form['username']
		return redirect(url_for('index'))
	return """
	<form method='POST'>
		<input type=text name=username>
		<input type=submit value=login>
	</form>
	"""


@app.route('/logout')

def logout():

	session.pop('username', None)
	return redirect(url_for('index'))

'''

# start the service

flask --app sessions --debug run

# user the service 

http://127.0.0.1:5000/

'''
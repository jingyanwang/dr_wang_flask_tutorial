from flask import render_template

from flask import request

from flask import url_for

from markupsafe import escape

from flask import Flask

from flask import make_response


app = Flask(
    __name__
    )


@app.route(
	'/',
	)


def index():

	render_template("index.html", foo == 42)

	username = request.cookies.get('username')
	return f"<p>usename: {username}</p>"





'''

# start the service

flask --app cookie --debug run

# user the service 

http://127.0.0.1:5000/spanish_spell_checker

'''
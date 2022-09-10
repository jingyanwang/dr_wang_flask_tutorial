from flask import render_template

from flask import request

from flask import url_for

from markupsafe import escape

from flask import Flask

from flask import make_response


from flask import abort, redirect, url_for


app = Flask(
    __name__
    )


@app.route(
	'/',
	)


def index():

	return redirect(url_for('login'))


@app.route(
	'/login',
	)

def login():
	abort(401)

@app.errorhandler(401)
def page_not_found(
	error,
	):
	return render_template('page_not_found.html'), 401


'''

# start the service

flask --app directions_and_errors --debug run

# user the service 

http://127.0.0.1:5000/

'''
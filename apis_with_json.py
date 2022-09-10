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


@app.route("/me")

def me_api():
	return {
		"username":"jingyan",
		"theme":"black"
	}


@app.route("/users")

def users_api():
	return [
		{
		"username":"jingyan",
		"theme":"black"
		},
		{
		"username":"john",
		"theme":"white"
		},
	]

'''

# start the service

flask --app apis_with_json --debug run

# user the service 

http://127.0.0.1:5000/

'''
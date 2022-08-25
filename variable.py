from markupsafe import escape

from flask import Flask

app = Flask(
    __name__
    )

@app.route("/user/<username>")

def show_user_profile(
	username,
	):
	return f"User {escape(username)}"


@app.route("/post/<int:post_id>")

def show_post(
	post_id,
	):
	return f"post {post_id}"


@app.route("/hello")

def hello(
	):
	return "Hello, world"


@app.route(
	"/path/<path:subpath>"
	)

def show_subpath(
	subpath,
	):
	return f"subpath {escape(subpath)}"

'''
flask --app variable --debug run --host=0.0.0.0 

http://10.94.245.169:5000/user/jingyan

http://10.94.245.169:5000/post/123

http://10.94.245.169:5000/path/this/is/a/test

'''
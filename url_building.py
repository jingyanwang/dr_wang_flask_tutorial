from flask import url_for

from markupsafe import escape

from flask import Flask

app = Flask(
    __name__
    )


@app.route(
	"/"
	)

def index():
	return 'index'

@app.route(
	"/login"
	)

def login(
	):
	return "login"


@app.route(
	"/user/<username>"
	)

def profile(
	username,
	):
	return f"{username}'s profile"


with app.test_request_context():
	print(url_for('index'))
	print(url_for('login'))
	print(url_for('login', next = '/'))
	print(url_for('profile', username = '/jingyan'))

'''

flask --app url_building --debug run --host=0.0.0.0 

http://10.94.245.169:5000/login

http://10.94.245.169:5000/user/jingyan

http://10.94.245.169:5000/about

http://10.94.245.169:5000/about/

'''
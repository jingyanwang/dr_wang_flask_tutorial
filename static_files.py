from flask import request

from flask import url_for

from markupsafe import escape

from flask import Flask

app = Flask(
    __name__
    )


'''
@app.route(
	"/login",
	methods = ["GET", "POST"]
	)

def login(
	):
	if request.method == "POST":
		return "do the login"
	else:
		return "show the login form"
'''


@app.get(
	"/login"
	)

def login_get():
	return "do the login new"


@app.post(
	"/login"
	)

def login_post():
	return "do the login new"


'''

flask --app static_files --debug run --host=0.0.0.0 


curl -X POST http://10.94.245.169:5000/login

C:\\Users\\jimwa>curl -X POST http://10.94.245.169:5000/login
do the login
C:\\Users\\jimwa>curl -X GET http://10.94.245.169:5000/login
show the login form
C:\\Users\\jimwa>


http://10.94.245.169:5000/login

http://10.94.245.169:5000/user/jingyan

http://10.94.245.169:5000/about

http://10.94.245.169:5000/about/

'''
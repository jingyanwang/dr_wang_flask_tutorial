from markupsafe import escape

from flask import Flask

app = Flask(
    __name__
    )

@app.route(
	"/projects/"
	)

def projects(
	):
	return "The project page"


@app.route(
	"/about"
	)

def about(
	):
	return "The about page"

'''

flask --app unique_url --debug run --host=0.0.0.0 

http://10.94.245.169:5000/projects/

http://10.94.245.169:5000/projects

http://10.94.245.169:5000/about

http://10.94.245.169:5000/about/

'''
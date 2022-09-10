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


@app.errorhandler(404)
def page_not_found(
	error,
	):
	resp = make_response(render_template('page_not_found.html'), 404)
	resp.headers['x-somthing'] = 'a value'
	return resp


'''

# start the service

flask --app about_responses --debug run

# user the service 

http://127.0.0.1:5000/

'''
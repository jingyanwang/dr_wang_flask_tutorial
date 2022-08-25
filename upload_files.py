from flask import render_template

from flask import request

from flask import url_for

from markupsafe import escape

from flask import Flask


from werkzeug.utils import secure_filename

app = Flask(
    __name__
    )


@app.route(
	'/upload',
	methods = [
		'POST',
		'GET',
		])

def upload_file():

	if request.method == 'POST':

		f = request.files['the_file']

		#f.save('uploaded_file.txt')

		f.save(
			f'{secure_filename(f.filename)}',
			)

		return render_template(
			"upload.html",
			status = "uploaded",
			)

	else:
		return render_template(
			"upload.html",
			status = "please upload",
			)


'''

flask --app upload_files --debug run --host=0.0.0.0 


http://10.94.245.169:5000/upload

curl -X POST http://10.94.245.169:5000/login

'''
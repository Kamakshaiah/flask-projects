from flask import Flask, render_template, request
import pandas
import os

app = Flask(__name__)

@app.route('/')
def home():
	return '''Home'''
@app.route('/importdata', methods=['GET','POST'])
def importdata():
	if request.method == "POST":
		df = request.files.get("df-file")
		rootdir = os.path.dirname(os.path.abspath(__file__))
		path = os.path.join(rootdir, df.filename)
		return render_template('tables.html', data=path)
	return render_template('tables.html')

if __name__ == '__main__':
	app.run(debug=True)

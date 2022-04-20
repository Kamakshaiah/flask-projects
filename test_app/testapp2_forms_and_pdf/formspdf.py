from flask import Flask, render_template, request

app = Flask(__name__)


studs = [
	{
		"id": "1",
		"name": "student 1",
		"class": "class 1",
	},
	{
		"id": "2",
		"name": "student 2",
		"class": "class 1",
	},
	{
		"id": "3",
		"name": "student 3",
		"class": "class 1",
	},
	{
		"id": "4",
		"name": "student 4",
		"class": "class 1",
	},

]

@app.route('/')
def home():
	return render_template('form.html')

@app.route('/data', methods=['GET','POST'])
def data():
	name = request.form["name"]
	email = request.form["email"]

	return render_template('data.html', name = name, email = email)

@app.route('/students')
def students():
	return render_template('students.html', students=studs)

if __name__ == '__main__':
	app.run(debug=True)

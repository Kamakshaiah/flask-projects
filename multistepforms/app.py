from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/data', methods = ['GET', 'POST'])
def data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        info = [name, email, password]

        return render_template('data.html', info = info)



if __name__ == '__main__':
    app.run(debug=True)

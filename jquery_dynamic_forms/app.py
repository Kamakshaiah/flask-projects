from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/dynamic', methods=['GET', 'POST'])
def dyanmic():
    if request.method == 'POST':
        val = request.form['val']
    return render_template('dynamic.html', val=int(val))


if __name__ == '__main__':
    app.run(debug=True)

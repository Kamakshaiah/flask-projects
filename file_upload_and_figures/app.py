from flask import Flask, render_template, request
import pandas as pd
import os, time
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods = ['GET','POST'])
def data():
    if request.method == 'POST':
        file = request.files['file']
        if not os.path.isdir('static'):
            os.mkdir('static')

        filename = os.path.join('static', file.filename)
        file.save(filename)
        return 'file saved'

@app.route('/dash',methods = ['GET','POST'] )
def dash():
    if request.method == 'POST':
        variable = request.form['varname']
        data = pd.read_csv(os.path.join('static', 'test.csv'))
        plt.plot(data[variable])
        figpath = os.path.join('static', time.strftime("%S" + '.png'))
        plt.savefig(figpath)
        return render_template('figure.html', figure = figpath)
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

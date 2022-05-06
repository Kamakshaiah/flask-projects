from flask import Flask, render_template, request
import os
import pandas as pd
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static', file.filename)
        file.save(filepath)
        return 'The file name of the uploaded file is: {}'.format(file.filename)
    return render_template('index.html')

@app.route('/dash', methods = ['GET', 'POST'])
def dash():
    if request.method == 'POST':
        variable = request.form['variable']
        data = pd.read_csv('static/test.csv')
        size = len(data[variable])
        plt.bar(range(size), data[variable])
        imagepath = os.path.join('static', 'image' + '.png')
        plt.savefig(imagepath)
        return render_template('image.html', image = imagepath)
    return render_template('dash.html')



if __name__ == '__main__':
    app.run(debug=True)

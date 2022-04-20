from flask import Flask, render_template, request
from form import InputForm
from computations import compute
import matplotlib.pyplot as plt
import numpy as np
import os, time

app = Flask(__name__)

@app.route('/')
def index():
    return '''This is test app'''

@app.route('/plotfile')
def plotfile():
    x = np.random.uniform(0, 1, 10)
    y = np.random.normal(0, 1, 10)

    plt.figure()
    plt.plot(x, y)
    plotfile = os.path.join(str(time.time())+'.png')
    plt.savefig(plotfile)
    return render_template('plot.html', result=plotfile)

if __name__ == '__main__':
    app.run()

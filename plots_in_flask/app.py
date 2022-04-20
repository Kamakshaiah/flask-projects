from flask import Flask, render_template
import os, time, glob
import matplotlib.pyplot as plt
import compute as cmt

app = Flask(__name__)

@app.route('/')
def index():
    if not os.path.isdir('static'):
        os.mkdir('static')

        filepath = os.path.join('static', str(time.time()) + '.png')

        plt.plot(cmt.compute_data(10, 10))
        plt.savefig(filepath)
        return render_template("plot.html", path = filepath)

if __name__ == '__main__':
    app.run(debug=True)

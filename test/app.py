from flask import Flask, render_template
import matplotlib.pyplot as plt
import compute as cmpt
import os, time, glob

app = Flask(__name__)

@app.route('/')
def index():
    path = os.path.join("static", "images")
    plt.plot(cmpt.create_data(10, 10))
    if not os.path.isdir(path):
        os.mkdir(path)
    else:
        for filename in glob.glob(os.path.join(path, "*.png")):
            os.remove(filename)
        filepath = os.path.join(path, str(time.strftime("%Y-%m-%d-%H-%M-%S"))+"-plot.png")
        plt.savefig(filepath)
        return render_template("index.html", fig = filepath)

if __name__ == '__main__':
    app.run(debug=True)

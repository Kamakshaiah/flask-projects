from flask import Flask, render_template, Response, url_for, request
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import io
import base64
import numpy as np
import pandas as pd
import string
import random as rnd
from wtforms import Form, IntegerField, validators

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

def define_df(dp = 10, nc=2):
    x = pd.DataFrame(np.random.randn(dp, nc))
    nrows = np.shape(x)[1]
    x.columns = list(string.ascii_lowercase[0:nrows])
    return x

class InputForm(Form):
    d = IntegerField(
        label = 'discrete series', default = 5, validators = [validators.InputRequired()]
    )
    c = IntegerField(
        label = 'Continous series', default = 5, validators = [validators.InputRequired()]
    )
    nr = IntegerField(
        label = 'No. of Rows', default = 10, validators = [validators.InputRequired()]
    )
    nc = IntegerField(
        label = 'No. of Columns', default = 5, validators = [validators.InputRequired()]
    )

@app.route('/simulations', methods = ['GET','POST'])
def simulations():
    form = InputForm(request.form)
    df = define_df(form.nr.data, form.nc.data)
    return render_template('simulations.html', table=df.to_html())

@app.route('/table', methods = ['POST','GET'])
def table():
    form = InputForm(request.form)
    if request.method == "GET" and form.validate():
        dat = define_df(form.d.data, form.nc.data)
        data = dat.to_html
        return render_template('table.html', name = "dataset", data = data)
        #return render_template('table.html', data=data)

# @app.route('/datasimform', methods = ['POST','GET'])
# def datasimform():
#     return render_template('simulations.html')
#
# # @app.route('/datasim', methods = ['GET'])
# @app.route('/table', methods = ['POST','GET'])
# def table():
#     # x = define_df()
#     # return render_template('table.html', name = 'dataset', data = x.to_html())
#
#     if request.method == 'GET':
#         d = request.args.get('discrete')
#         c = request.args.get('continous')
#         nr = request.args.get('m')
#         nc = request.args.get('n')
#         v = request.args.get('vector') == 'Vector'
#         m = request.args.get('matrix') == 'Matrix'
#
#         # return 'discrete'+'\t'+d + '\t' +c+'\t' +nr+'\t' +nc
#         # if (v):
#         # df = np.random.randn(1, int(d), int(nr))
#         # dat = pd.DataFrame({'x':df})
#             # return render_template('table.html', name = 'dataset', data = dat.to_html())
#         return
#     #
#     #     else:
#     #         df = np.random.randn(1, 5, 10)
#     #         dat = pd.DataFrame({'x':df})
#     #         return render_template('table.html', name = 'dataset', data = dat.to_html())



@app.route('/plots')
def build_plot():

    img = io.BytesIO()


    x = np.arange(0, 10)
    y = np.random.normal(0, 1, 10)

    plt.plot(x, y, '-o')

    plt.subplot(2, 1, 1)
    plt.plot(x, y, '-o')
    plt.subplot(2, 1, 2)
    y1 = np.random.normal(0, 1, 10)
    plt.plot(x, y1, '-o')

    plt.savefig(img, format = 'png')

    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png; base64, {}">'.format(plot_url)

@app.route('/test')
def chartTest():
  lnprice=np.log(np.arange(1, 10))
  plt.plot(lnprice)
  plt.savefig('static/images/plot1.png')
  return render_template('test.html', name = 'plot1', url = url_for('static', '/images/plot1.png'))


if __name__ == '__main__':
    app.run(debug = True)

from flask import Flask, render_template, url_for, request, make_response
from flask_wkhtmltopdf import Wkhtmltopdf
import pdfkit
import os
import requests
import pandas as pd
import numpy as np
import random

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

app = Flask(__name__)
app.config['PDF_FOLDER'] = 'static/'
app.config['TEMPLATE_FOLDER'] = 'templates/'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        wts = request.form['weights']
        nc = request.form['numberOfClasses']
        subs = request.form['subjects']

        sp = request.form['shape']

        wtslist = wts.split(',')
        subslist = subs.split(',')

        splist = sp.split(',')
        print(splist)

        clses = random.choices(subslist, k=int(nc))
        orderedclses = np.array(clses)
        #shape=[5, 4]
        oc = orderedclses.reshape([int(splist[0]), int(splist[1])])

        return render_template('view.html', tt = oc)

@app.route('/viewtt', methods=['GET', 'POST'])
def viewtt():
    if request.method == 'POST':
        form = request.form.getlist("subvalue")
        form = np.array(form)
        #print(type(form))
        #print(form[0])
        return render_template('viewtt.html', form = form)

@app.route('/ttpdf', methods=['GET', 'POST'])
def ttpdf():
    if request.method == 'POST':
        rendered = render_template("viewtt.html")
        url = request.form['url']
        pdf = pdfkit.from_file(url, False, configuration=config)
        response = make_response(pdf)

        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
        return response
        #render_template_to_pdf('viewtt.html', download=True, save=False)

if __name__ == '__main__':
    app.run(debug=True)

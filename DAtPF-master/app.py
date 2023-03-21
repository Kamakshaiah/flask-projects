from flask import Flask, render_template, jsonify, request, url_for, send_file
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
import calc

app = Flask(__name__)
app.secret_key = "this is secrete key"


class variablesForm(FlaskForm):
	var1 = TextField("Var 1")
	var2 = TextField("Var 2")
	submit = SubmitField("Submit")
	
@app.route("/")
def home():
	return '''This is home'''
	
@app.route("/tables/")
def tables():
	df = calc.define_table()
	return df.to_html()
	
@app.route("/ttest/", methods = ['GET','POST'])
def ttest():
	
	df = calc.define_table()
	dfhead = df.head()
	mysum = calc.describe(df)
	names = calc.names(df)
	
	form = variablesForm()
	
	if request.method == "POST":
		
		x = form.var1.data
		y = form.var2.data
		
		out = [x,y]
		
		path1 = calc.makeHist(df[x])
		path2 = calc.makeHist(df[y])
		ttest = calc.t_test(df[x], df[y])
		
		return render_template("summaries.html", form = form, out=dfhead.to_html(), out1 = mysum.to_html(), out2 = names, out3 = out, graph1 = path1, graph2 = path2, ttest=ttest) 
		
	return render_template("summaries.html", form = form, out=dfhead.to_html(), out1 = mysum.to_html(), out2 = names) 
	
if __name__ == '__main__':
	app.run(debug=True)

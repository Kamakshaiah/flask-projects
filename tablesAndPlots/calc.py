import pandas as pd
from scipy import stats
import io
import base64
import matplotlib.pyplot as plt
import pygal
import plotly.express as px

def define_table():
	df = pd.read_csv("sampledata.csv")
	return df

def describe(df):
	return df.describe()

def names(df):
	return df.columns
	
def t_test(x, y):
	return stats.ttest_ind(x, y)
	
def makehist(x, df):
	hist = pygal.Histogram()
	hist.add(x, df[x])
	return hist.render_data_uri() 
	
def makeHist(x):
	img = io.BytesIO()
	plt.hist(x, align='mid')
	plt.grid(True)
	plt.legend()
	plt.savefig(img, format='png')
	img.seek(0)
	url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	
	return "data:image/png;base64,{}".format(url)
	
def makePXHist(x):
	img = io.BytesIO()
	px.histogram(x)
	fig.savefig(img, format='png')
	img.seek(0)
	url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	
	return "data:image/png;base64,{}".format(url)
	

def makeGraph(xvar):
	img = io.BytesIO()
	
	plt.hist(xvar)
	plt.savefig(img, format='png')
	img.seek(0)
	img_url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	return 'data:image/png;base64,{}'.format(img_url)

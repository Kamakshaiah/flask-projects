from flask import Flask, render_template, request, Response
from requests.exceptions import HTTPError

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/data', methods = ['GET','POST'])
def data():
    try:
        if request.method == 'POST':
            data = request.form['data']
            #data.raise_for_status()
            return '''the data is {}'''.format(data)
    except :
        return Response("this is 400 bad request", status = 400)



if __name__ == '__main__':
    app.run(debug=True)

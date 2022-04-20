from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import copy

app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        file = request.form['file']
        ques = pd.read_excel(file)
        questions = ques.to_dict()
        questions = copy.deepcopy(questions)

        return render_template('questions.html', questions=questions.values())

if __name__ == '__main__':
    app.run(debug=True)

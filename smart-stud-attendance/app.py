from flask import Flask, render_template, request
import pandas as pd

import calculate as calc

app = Flask(__name__)

@app.route('/')
def index():

    regnos = calc.regNums(10)
    names = calc.names(10)
    places = calc.place(10)
    courses = calc.course(10)
    #df = pd.DataFrame({'regnos': regnos, 'names': names})
    info = {'regnos': regnos, 'names': names, 'places': places, 'courses': courses}
    df = pd.DataFrame(info)
    return render_template('index.html', df=df)

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        present = request.form.getlist('present')
        absent = request.form.getlist('absent')
        regnos = calc.regNums(10)
        #pd.DataFrame({"regnos": regnos)
        return render_template('attendance.html', attend=[present, absent])


if __name__ == '__main__':
    app.run(debug=True)

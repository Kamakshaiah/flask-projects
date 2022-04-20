from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salesdb.db'
db = SQLAlchemy(app)


class sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    email_id = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20))
    age = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    items = db.Column(db.Integer, nullable=False)
    items = db.Column(db.String, nullable=False)
    purchase = db.Column(db.Integer, nullable=False)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entryform')
def entryform():
    return render_template('entryform.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)

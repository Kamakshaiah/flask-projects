from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(15))

    def __repr__(self):
        return f"register('{self.name}', '{self.email}')"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = register(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'You are registered successfully!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

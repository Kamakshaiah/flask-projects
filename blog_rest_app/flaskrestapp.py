from flask import Flask, request, render_template, flash, url_for, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e440e4b3ec3de7f99b74110b6ee19af6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    """docstring for ."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    """docstring for Post."""
    id = db.Column(db.Integer, primary_key=True)


    def __init__(self, arg):
        super(Post, self).__init__()
        self.arg = arg

products_desc = [
    {
        "name": "product1",
        "make": "domestic",
        "price": 123,
        "quantity": 23
    },
    {
        "name": "product2",
        "make": "domestic",
        "price": 133,
        "quantity": 13
    },
    {
        "name": "product3",
        "make": "international",
        "price": 144,
        "quantity": 3
    },
    {
        "name": "product4",
        "make": "domestic",
        "price": 154,
        "quantity": 43
    },
    {
        "name": "product5",
        "make": "international",
        "price": 122,
        "quantity": 13
    },
    {
        "name": "product6",
        "make": "domestic",
        "price": 143,
        "quantity": 12
    },
    {
        "name": "product7",
        "make": "domestic",
        "price": 115,
        "quantity": 3
    },
    {
        "name": "product8",
        "make": "international",
        "price": 144,
        "quantity": 3
    },
    {
        "name": "product9",
        "make": "domestic",
        "price": 154,
        "quantity": 43
    },
    {
        "name": "product10",
        "make": "international",
        "price": 123,
        "quantity": 23
    }
]

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/blog')
def products():
    prods = products_desc()

    return render_template('products.html', title='Blog', products=prods)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Success', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'password':
            flash(f'You have been loggedin', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Check email and password!', 'danger')
    return render_template('login.html', title = 'Login', form=form)



if __name__ == '__main__':
    app.run()

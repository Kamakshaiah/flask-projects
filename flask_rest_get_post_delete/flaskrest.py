from flask import Flask, request, jsonify, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
import uuid
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(100))
    name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    user_password = db.Column(db.String(50))
    admin_check = db.Column(db.Boolean)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/products', methods=['GET'])
def get_all_products():

    prods = Product.query.all()
    output = []

    for prod in prods:
        prod_data = {}
        prod_data['product_id'] = prod.product_id
        prod_data['name'] = prod.name
        prod_data['quantity'] = prod.quantity
        prod_data['price'] = prod.price
        output.append(prod_data)
    return jsonify({'products' : output })

@app.route('/products/<product_id>', methods=['GET'])
def get_one_product(product_id):

    prod = Product.query.filter_by(product_id=product_id).first()

    if not prod:
        return jsonify({'message' : 'No Product with that ID!'})

    prod_data = {}
    prod_data['product_id'] = prod.product_id
    prod_data['name'] = prod.name
    prod_data['quantity'] = prod.quantity
    prod_data['price'] = prod.price

    return jsonify({'Product' : prod_data })

@app.route('/products', methods=['POST'])
def create_product():

    data = request.get_json()
    new_prod = Product(product_id=str(uuid.uuid4()), name=data['name'], quantity=data['quantity'], price=data['price'])
    db.session.add(new_prod)
    db.session.commit()

    return jsonify({'message': 'New Product Created'})

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):

    prod = Product.query.filter_by(product_id=product_id).first()

    if not prod:
        return jsonify({'message' : 'No Product with that ID!'})

    db.session.delete(prod)
    db.session.commit()

    return jsonify({'message': 'The product is being deleted!'})

@app.route('/users', methods=['POST'])
def add_user():
    user = request.get_json()

    new_user = User(user_name = user['name'], user_password=user["password"], admin_check = False   )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user has beeen created'})

@app.route('/users', methods=['GET'])
def get_users():

    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['user_name'] = user.user_name
        user_data['user_password'] = user.user_password
        user_data['admin_check'] = user.admin_check
        output.append(user_data)

    return jsonify({'users': output})

@app.route('/users/<user_name>', methods=['DELETE'])
def delete_user(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    if not user:
        return jsonify({'message': 'No user!'})
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted!'})

@app.route('/users/<user_name>', methods=['PUT'])
def promote_user(user_name):

    user = User.query.filter_by(user_name=user_name).first()
    if not user:
        return jsonify({'message': 'No user!'})

    user.admin_check = True
    db.session.commit()

    return jsonify({'message': 'User promoted!'})

@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(user_name=auth.username).first()
    if not user:
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if user.admin_check == True:
        token = jwt.encode({'user_name': user.user_name, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return jsonify({'message': 'The user is not authorized!'})



if __name__ == '__main__':
    app.run(debug=True)

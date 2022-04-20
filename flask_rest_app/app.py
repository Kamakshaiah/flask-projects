from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

langs = [
    {'name':'python', 'desc':'very best for data science', 'rank': 1},
    {'name':'R', 'desc': 'very best for data analytics', 'rank': 2},
    {'name':'java', 'desc': 'very best for applications', 'rank': 3}
    ]

prods = [
    {
        'name':'product1',
        'desc':'domestic',
        'price': 112,
        'quantity': 23
        },
    {
        'name':'product2',
        'desc': 'abroad',
        'price': 209,
        'quantity': 13
        },
    {
        'name':'product3',
        'desc': 'domestic',
        'price': 233,
        'quantity': 14
        },
    {
        'name':'product4',
        'desc':'domestic',
        'price': 112,
        'quantity': 23
        },
    {
        'name':'product5',
        'desc': 'abroad',
        'price': 209,
        'quantity': 13
        },
    {
        'name':'product6',
        'desc': 'domestic',
        'price': 233,
        'quantity': 14
        }, 
     {
        'name':'product7',
        'desc': 'domestic',
        'price': 233,
        'quantity': 14
        },
    {
        'name':'product8',
        'desc':'domestic',
        'price': 112,
        'quantity': 23
        },
    {
        'name':'product9',
        'desc': 'abroad',
        'price': 209,
        'quantity': 13
        },
    {
        'name':'product10',
        'desc': 'domestic',
        'price': 233,
        'quantity': 14
        }
    ]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/langs', methods=['GET'])
def langs_data():
    return jsonify({'laguages': langs})

@app.route('/prods', methods=['GET'])
def prods_data():
    return jsonify({'products': prods})

@app.route('/prods/price', methods=['GET'])
def prods_data_additional():
    products = []
    for i in range(0, len(prods)):
        products.append(prods[i]["name"])
    price = []
    for i in range(0, len(prods)):
        price.append(prods[i]["price"])
    price_dict = dict(zip(products, price))

    return jsonify({'price_data': price_dict})


if __name__ == '__main__':
    app.run(debug=True)

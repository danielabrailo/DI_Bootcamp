import json
import os

import products_data
from flask import Flask, render_template

app = Flask(__name__)

cart_json = 'cart.json'


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/products')
def products():
    products_list = products_data.retrieve_all_products()
    return render_template('products.html', info=products_list)


@app.route('/products/<product_id>')
def prod_details(product_id):
    products_list = products_data.retrieve_all_products()
    return render_template('prod_details.html', info=products_list, prod_id=product_id)


@app.route('/cart')
def cart():
    with open(cart_json, 'r') as f:
        cart_items = json.load(f)
    return render_template('cart.html', cart_item=cart_items)


@app.route('/add_product_to_cart/<product_id>/<name>/<price>')
def add_product(product_id, name, price):
    new_data = {'product_id': product_id, 'name': name, 'price': price}
    with open(cart_json, 'w+') as file:
        if os.stat(cart_json).st_size == 0:
            file_data = new_data
        else:
            file_data = json.load(file)
            file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file)
    with open(cart_json, 'r') as f:
        cart_products = json.load(f)
    return render_template('cart.html', cart_item=cart_products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

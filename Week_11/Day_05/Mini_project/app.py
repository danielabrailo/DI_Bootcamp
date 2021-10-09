import products_data
from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True, port=5000)

import json

from flask import Flask, render_template

app = Flask(__name__)


def load_database(src_file='product_db.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/products')
def products():
    info = load_database()
    return render_template('products.html', products=info)


@app.route('/product/<product_id>')
def prod_details(product_id):
    info = load_database()
    return render_template('prod_details.html', products=info, prod_id=product_id)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

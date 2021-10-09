import json


def retrieve_all_products():
    json_file = 'products.json'
    with open(json_file, 'r') as f:
        all_products = json.load(f)
        return all_products


def retrieve_requested_product(product_id):
    all_products = retrieve_all_products()
    for product in all_products.read():
        if product.id == product_id:
            requested_product = product
            return requested_product



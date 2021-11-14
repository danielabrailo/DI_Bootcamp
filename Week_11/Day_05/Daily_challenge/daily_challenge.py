import requests
from flask import Flask, render_template

app = Flask(__name__)

types_res = requests.get('https://pokeapi.co/api/v2/type')
types_data = types_res.json()
types = types_data['results']


@app.route('/')
def main():
    return render_template('home.html', info=types)


@app.route('/pokemons/bytype/<type>')
def by_type(type):
    for x in types:
        if x['name'] == type:
            types_res = requests.get(x['url'])
            types_data = types_res.json()
    return render_template('type.html', info=types_data)


@app.route('/pokemon/<id>')
def pok_id(id):
    types_res = requests.get('https://pokeapi.co/api/v2/pokemon/<id>')
    types_data = types_res.json()
    return render_template('pokemon.html', info=types_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

import requests
from flask import Flask, render_template

app = Flask(__name__)

types_res = requests.get('https://pokeapi.co/api/v2/type')
types_data = types_res.json()
types = types_data['results']
all_pokemon_get = requests.get('https://pokeapi.co/api/v2/pokemon/')
all_pokemon = all_pokemon_get.json()
all_pokemon_list = all_pokemon['results']


@app.route('/')
def main():
    return render_template('home.html', info=types)


@app.route('/pokemons/bytype/<type>')
def by_type(type):
    for x in types:
        if x['name'] == type:
            types_get = requests.get(x['url'])
            types_list = types_get.json()
            return render_template('type.html', info=types_list)


@app.route('/pokemon/<id>')
def pok_id(id):
    id_res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    id_data = id_res.json()
    return render_template('pokemon.html', info=id_data)


@app.route('/pokemons/byname/<name>')
def by_name(name):
    for x in all_pokemon_list:
        if x['name'] == name:
            name_res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
            name_data = name_res.json()
            return render_template('pokemon.html', info=name_data)
    else:
        return render_template('home.html', info=types)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

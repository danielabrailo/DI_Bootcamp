import json

with open('file.json', 'r+') as f:
    family = json.load(f)
    for child in family['children']:
        print(f'the name of the child is {child["firstName"]} and the age is {child["age"]}')
        child['favorite_color'] = 'red'

    f.flush()  # removes the content of the file
    f.seek(0)
    json.dump(family, f, indent=2)

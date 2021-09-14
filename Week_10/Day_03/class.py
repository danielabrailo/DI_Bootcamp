with open("nameslist.txt", "r") as f:
    # read line by line
    print(f.read())
    # Read only the 5th line of the file
    files = f.readlines()
    print(files[4])
    # Read all the file and return it as a list of strings. Then split each word
    files = f.readlines()
    print(files)
    # Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
    files = f.read().splitlines()
    print(files)
    print(files.count('Lea'))
    # Append "SkyWalker" next to each first name "Luke"
with open('nameslist.txt', 'r+') as f:
    files = f.read().splitlines()
    for i in range(len(files)):
        if files[i] == 'Luke':
            files.insert(i+1, 'SkyWalker')
    f.seek(0)
    f.write('\n'.join(files))


# API Exercise
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
print(response.json()['value'])


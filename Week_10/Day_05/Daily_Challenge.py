# Function that returns the amount of time it takes a webpage to load
import requests


def time_to_load():
    time = requests.get('https://www.google.com').elapsed.total_seconds()
    print(f'The time it took to load the page is {round(time,2)} seconds')


time_to_load()
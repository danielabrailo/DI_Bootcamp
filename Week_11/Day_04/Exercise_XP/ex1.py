from flask import Flask, render_template
import datetime

app = Flask(__name__)

current_time = datetime.datetime.now()
greeting = ' '
if 13 > current_time.hour >= 8:
    greeting = 'Good morning!'
elif 17 > current_time.hour >= 13:
    greeting = 'Good afternoon!'
elif 21 > current_time.hour >= 17:
    greeting = 'Good evening!'
elif 8 > current_time.hour >= 21:
    greeting = 'Good night!'


@app.route('/')
def main():
    return render_template('greeting.html', message=greeting)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

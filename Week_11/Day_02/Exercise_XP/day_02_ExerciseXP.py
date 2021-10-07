import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Daniela's CV"


@app.route('/hobbies')
def hobbies():
    return flask.render_template('hobbies.html')


@app.route('/skills')
def skills():
    return flask.render_template('skills.html')


@app.route('/strengths')
def strengths():
    return flask.render_template('strengths.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

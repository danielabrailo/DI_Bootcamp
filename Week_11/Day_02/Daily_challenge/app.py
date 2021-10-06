import flask
from flask import render_template_string

app = flask.Flask(__name__)


@app.route('/exercises')
def exercise_page():
    exercises_content = open('exercises.md', 'r').read()
    return render_template_string(exercises_content)


@app.route('/in-this-chapter')
def main():
    in_this_chapter_content = open('in-this-chapter.md', 'r').read()
    return render_template_string(in_this_chapter_content)


if __name__ == "__main__":
    app.run()

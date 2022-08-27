from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'abchello'

toolbar = DebugToolbarExtension(app)

@app.route('/words-for-madlib')
def create_form():
    return render_template('form.html', words=story.prompts)

@app.route('/complete-story')
def show_complete_story():
    ans =request.args
    return render_template('story.html', story=story.generate(ans))
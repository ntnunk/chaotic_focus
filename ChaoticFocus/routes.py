from flask import render_template, flash, redirect, url_for
from ChaoticFocus import app

posts = [
        {
            'datetime': '2017-10-20T11:33:00-04:00',
            'author': 'Noel',
            'category': 'Cycling',
            'tags': ['cycling', 'offseason', 'mtb'],
            'slug': "Still firmly in offseason mode, I'm heading to the mountains",
            'content': "This is the post body for post #1"
        },
        {
            'datetime': '2017-10-06T10:00:00-04:00',
            'author': 'Noel',
            'category': 'Cycling',
            'tags': ['cycling', 'offseason'],
            'slug': "My offseason came pretty suddenly for me this year.",
            'content': "This is the post body for post #2"
        }
    ]

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', title='Chaotic Focus', posts=posts)

@app.route('/about')
def about():
    render_template('about.html', title='About Me')

@app.route('/general')
def category_general():
    pass

@app.route('/tech')
def category_tech():
    pass

@app.route('/cycling')
def category_cycling():
    pass

@app.route('/woodworking')
def category_woodworking():
    pass

@app.route('/smart-fan')
def proj_smartfan():
    pass

@app.route('/led_cube')
def proj_led_cube():
    pass

@app.route('/dog_bed')
def proj_dog_bed():
    pass
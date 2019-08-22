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
    return render_template('home.html', title='Chaotic Focus')

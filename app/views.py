from flask import render_template
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html',
	title='Sign In',
	form=form)
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        { 
            'author': {'nickname': 'Jake'}, 
            'body': 'I liked Tarkovskys Solyaris!' 
        },
        { 
            'author': {'nickname': 'Danny'}, 
            'body': 'I liked the Matrix Better!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

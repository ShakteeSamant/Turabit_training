from application import app
from flask import render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy


@app.route('/')
@app.route('/enter')
def enter():
    return render_template('enter.html')


@app.route('/hello/')
def hello():
    return render_template('hello.html', title='Home')


@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            flash('Thank you for log in ')
            return redirect(url_for('home'))
    return render_template('login.html', error=error, title= 'Login')


@app.route('/register')
def register():
    return render_template('register.html', title='Register Page')

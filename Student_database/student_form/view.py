from flask import render_template, request, url_for
from student_form import app

@app.route('/')
def home():
    return 'Home Page'

@app.route('/form')
def form():
    return render_template('form.html')

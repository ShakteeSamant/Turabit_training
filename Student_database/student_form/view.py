from flask import render_template, request, url_for,redirect
from student_form import app,db
from student_form.models.model import Student_info

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/form')
@app.route('/add_student', methods= ['POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        sem = request.form['sem']
        mob_no = request.form['mob_no']
        email = request.form['email']
        add_stud = Student_info(name,roll_no,sem,mob_no,email)
        db.session.add(add_stud)
        db.session.commit()
        return render_template('home.html')
    else:
        return render_template('form.html')



from flask import render_template, request, url_for, redirect
from student_form import app, db
from student_form.models.model import Student_info


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/add_student', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        s_name = request.form['name']
        s_roll_no = request.form['roll_no']
        s_sem = request.form['sem']
        s_mob_no = request.form['mob_no']
        s_email = request.form['email']
        student = Student_info(name=s_name, roll_no=s_roll_no, sem=s_sem, mob_no=s_mob_no, email=s_email)
        db.session.add(student)
        db.session.commit()
        return render_template('show.html', name=s_name, roll_no=s_roll_no, sem=s_sem, mob_no=s_mob_no, email=s_email)
    else:
        return render_template('form.html')


@app.route('/student_list', methods=['GET', 'POST'])
def student_list():
    list_ = Student_info.query.all()
    return render_template('show_list.html', list_=list_)


@app.route('/edit/<int:s_id>', methods=['GET', 'POST'])
def edit(s_id):
    if request.method == 'GET':
        student = Student_info.query.filter_by(s_id=s_id).first()
        dict_ = {"s_id": student.s_id, "s_name": student.name, "s_roll_no": student.roll_no, "s_sem": student.sem,
                 "s_mob_no": student.mob_no, "s_email": student.email}
    return render_template('edit.html', request=dict_)


@app.route('/update/<int:s_id>', methods=['GET', 'POST'])
def update(s_id):
    if request.method == 'POST':
        new_name = request.form['new_name']
        new_roll_no = request.form['new_roll_no']
        new_sem = request.form['new_sem']
        new_mob_no = request.form['new_mob_no']
        new_email = request.form['new_email']
        student = Student_info.query.filter_by(s_id=s_id).update(dict(name = new_name,roll_no = new_roll_no,sem = new_sem,mob_no = new_mob_no,email = new_email))
        print(student)
        db.session.commit()
    return redirect(url_for('student_list'))


@app.route('/delete/<int:s_id>', methods=['GET', 'POST'])
def delete(s_id):
    if request.method == 'GET':
        student = Student_info.query.filter_by(s_id=s_id).first()
        db.session.delete(student)
        db.session.commit()
    return redirect(url_for('student_list'))

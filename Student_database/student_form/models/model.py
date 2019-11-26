from student_form import db


class Student_info(db.Model):
    __tablename__ = 'student_info'
    s_id = db.Column('s_id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(30), nullable=False)
    roll_no = db.Column('roll_no', db.String(10), nullable=False)
    sem = db.Column('sem', db.Integer, nullable=True)
    mob_no = db.Column('mob_no', db.String(60), nullable=False)
    email = db.Column('email', db.String(60), nullable=False)

    def __init__(self, name, roll_no, sem, mob_no, email):
        self.name = name
        self.roll_no = roll_no
        self.sem = sem
        self.mob_no = mob_no
        self.email = email

    # def __repr__(self):
    #     return f'''
    #     S_ID: {self.s_id},
    #     Name: {self.name},
    #     Rollno: {self.roll_no},
    #     Mobile: {self.mob_no},
    #     E-Mail: {self.email}
    #     '''

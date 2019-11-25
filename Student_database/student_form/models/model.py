from student_form import db

class Student_info(db.Model):
    __tablename__= 'student_info'
    s_id = db.Column('s_id', db.Integer , primary_key = True)
    name = db.Column('name', db.String(30), nullable= False)
    roll_no = db.Column('roll_no', db.String(10),unique=True, nullable= False)
    sem = db.Column('sem', db.Integer, nullable= True)
    mob_no = db.Column('mob_no', db.Integer, nullable= False)
    email = db.Column('email', db.String(60),unique=True, nullable= False)

    def __repr__(self):
        return f'Name:{self.name},Roll no.:{self.roll_no},Email ID:{self.email}'


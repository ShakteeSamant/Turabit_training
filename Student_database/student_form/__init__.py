from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5ce6a803fa8564b391bf9db642914667'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/student_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


from student_form import view
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3305/asch'
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.username}-{self.email}'


# if __name__ == '__main__':
#     app.run(debug=True)


# Note how we never defined a __init__ method on the User class? That’s because SQLAlchemy adds an implicit constructor to all model classes which accepts keyword arguments for all its columns and relationships. If you decide to override the constructor for any reason, make sure to keep accepting **kwargs and call the super constructor with those **kwargs to preserve this behavior:
#
# class Foo(db.Model):
#     # ...
#     def __init__(**kwargs):
#         super(Foo, self).__init__(**kwargs)
#         # do custom stuff


#
# (flask_env) E:\Turabit_Training\my_project\SQLAlchemy_Project>python
# Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from project1 import db
# E:\Turabit_Training\flask_env\lib\site-packages\flask_sqlalchemy\__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the
#  future.  Set it to True or False to suppress this warning.
#   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
# >>> db.create_all()
# >>> from project1 import user
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'user'
# >>> from project1 import User
# >>> user1 = User(username='admin', email='admin@example.com')
# >>> user2 = User(username='Shaktee', email= 'shaktee@email.com')
# >>> db.session.add(user1)
# >>> db.session.add(user2)
# >>> db.session.commit()
# >>> User.query.all()
# [admin-admin@example.com, Shaktee-shaktee@email.com]
# >>> User.query.filter_by(username='shaktee').first()
# Shaktee-shaktee@email.com
# >>>

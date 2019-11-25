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

# flask_env) E:\Turabit_Training\my_project\SQLAlchemy_Project>python -m pip install --upgrade pip
# Collecting pip
#   Downloading https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl (1.4MB)
#     100% |████████████████████████████████| 1.4MB 527kB/s
# Installing collected packages: pip
#   Found existing installation: pip 10.0.1
#     Uninstalling pip-10.0.1:
#       Successfully uninstalled pip-10.0.1
#   Rolling back uninstall of pip
# Exception:
# Traceback (most recent call last):
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_internal\basecommand.py", line 228, in main
#     status = self.run(options, args)
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_internal\commands\install.py", line 335, in run
#     use_user_site=options.use_user_site,
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_internal\req\__init__.py", line 49, in install_given_reqs
#     **kwargs
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_internal\req\req_install.py", line 748, in install
#     use_user_site=use_user_site, pycompile=pycompile,
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_internal\req\req_install.py", line 961, in move_wheel_files
#     warn_script_location=warn_script_location,
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_internal\wheel.py", line 431, in move_wheel_files
#     generated.extend(maker.make(spec))
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_vendor\distlib\scripts.py", line 403, in make
#     self._make_script(entry, filenames, options=options)
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_vendor\distlib\scripts.py", line 307, in _make_script
#     self._write_script(scriptnames, shebang, script, filenames, ext)
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_vendor\distlib\scripts.py", line 243, in _write_script
#     launcher = self._get_launcher('t')
#   File "E:\Turabit_Training\flask_env\lib\site-packages\pip-10.0.1-py3.6.egg\pip\_vendor\distlib\scripts.py", line 382, in _get_launcher
#     result = finder(distlib_package).find(name).bytes
# AttributeError: 'NoneType' object has no attribute 'bytes'
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

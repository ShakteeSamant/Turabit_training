from flask import Flask

app = Flask(__name__)
app.secret_key='53da20c96e3344038091922e38ecf457'


from application import routes

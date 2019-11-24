from flask import Flask

app = Flask(__name__)
app.secret_key='shaktee'


from application import routes

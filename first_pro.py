from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def home():
    return '''
    <h1>Turabit Solution PVT. LTD.</h1>
    '''

@app.route('/about')
@app.route('/about us')
def about():
    return 'TURABIT IS A TECHNOLOGY COMPANY THAT BELIEVES IN MAKING IT EASY FOR BUSINESSES TO CARE FOR THEIR CUSTOMERS, EVERYWHERE.'

@app.route('/user/<username>')
def show_user_profile(username):
# show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
# show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
# show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/uuid/<uuid:uuid_id>')
def uuid_path(uuid_id):
# show the UUID String
    return f'UUID is {uuid_id}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/user1/<username>')
def user(username):
# show the user profile for that user
    return render_template('first_pro.html', username= username)

@app.route('/user2/')
@app.route('/user2/<name>')
def user2(name=None): # here name = none is very imp. 
    return render_template('hello_from_flask.html', name= name)

if __name__=='__main__':
    app.run(debug=True)

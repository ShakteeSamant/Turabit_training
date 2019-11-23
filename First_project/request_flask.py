from flask import Flask, request
app = Flask(__name__)

@app.route('/query_example')
def query_example():
    language = request.args.get('language')  # i will return a None vale if not passed
    framework = request.args['framework'] # value  ust be passed

    return f'''
        <h1>the Language is {language}</h1>
        <h1>the Framework is {framework}</h1>
    '''
# http://127.0.0.1:5000/query_example?language=python&framework=flask

@app.route('/form_example', methods = ['GET','POST'])
def form_example():
    if request.method =='POST':
        language = request.form.get('language')
        framework = request.form['framework']
        return f'''<h1>Form Submitted</h1>
        <h3>Language = {language}</h3>
        <h3>Framework = {framework}</h3>
        '''
    
    return '''
        <form method ='POST'>
        Language <input type='text' name='language'>
        Framework <input type='text' name='framework'> 
        <input type='submit'>
        </form>
    '''
    #if the name diff then the object then it will return in get() and 404 error in form[]
# http://127.0.0.1:5000/form_example

from flask import Markup
@app.route('/mark')
def mark():
    return Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
    Markup.escape('<blink>hacker</blink>')
# Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')
    Markup('<em>Marked up</em> &raquo; HTML').striptags() 
# u'Marked up \xbb HTML'


if __name__=='__main__':
    app.run(debug=True)
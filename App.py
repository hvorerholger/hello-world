#realpython recipy on https://realpython.com/blog/python/developing-with-bottle-part-1/

import os
from bottle import Bottle, route, run, get, post, request, route, template, response

app = Bottle()

#Installation-----------------------------------------------
#https://gist.github.com/mjhea0/5784132 #zie persoonlijke notities

#Quickstart--------------------------------------------------
#helloWorld--------------------------------------------------
@app.route('/hello')
def hello():
    return "<h1>Hello1 World!</h1>"


#MyFirstWebApp-----------------------------------------------
@app.route('/<unknown>')
def dynamicRouting(unknown):
    return 'Houston we have a problem - return to home'

index_html = '''My first web app! By {{ author }}'''

#@app.route('/:anything')
def something(anything=''):
    return template(index_html, author=anything)

@app.route('/')
def index():
    return template(index_html, author='Walter Van Mulders')


#httpRequest--------------------------------------------------
@app.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login (uid,pwd):
    if uid == 'walter' and pwd == 'pass':
        return True
    else:
        return False


#WSGI_Environment---------------------------------------------
@app.route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    return template("Your IP is: {{ip}}", ip=ip)


#cookies-------------------------------------------------------
@app.route('/counter')
def counter():
    count = int( request.cookies.get('counter', '0') )
    count += 1
    response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count


    
#--------------------------------------------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(app, host='0.0.0.0', port=port, debug=True)

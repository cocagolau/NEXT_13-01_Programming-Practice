from flask import Flask, url_for, session, escape, request, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index () :
	if 'username' in session :
		return 'Logged in as %s <p><a href="/logout">logout</a>' % escape (session ['username'])
	return 'You are not logged in <p> <a href="/login"> login </a>'

@app.route('/student/<username>/')
def student (username) :
	return 'Hello %s' % username

@app.route ('/student/<username>/<int:user_id>')
def student_with_id (username, user_id) :
	return 'Hello %s, %d' % (username, user_id)

@app.route ('/method', methods=['GET','POST'])
def test_HTTP_method () :
	if request.method == 'POST' :
		return request.method
	else :
		return request.method + '<p>' + request.args.get('name') + '<p>' + request.args.get('password')

@app.route ('/login', methods=['POST','GET'])
def login () :
	try :
		if request.method == 'POST' :
			name = request.form ['name']
			passwd = request.form ['password']
			if name :
				session ['username'] = name
			return render_template ('login.html', username = session['username'])
		else :
			return render_template ('login.html')

	except KeyError, err :
		print 'error -> :', err
		return 'ERROR im'

@app.route ('/logout')
def logout () :
	session.pop ('username', None)
	return redirect (url_for('index'))

if __name__ == '__main__':
	app.debug = True
	app.secret_key = "\xb7x\xc2\x1eoA\xc9\xade\x91\xfc\x86{\x94Bs\xd0$\xd4\xb4D\xb9\xe0"
	app.run(host='127.0.0.1')




import sqlite3, smtplib, os, subprocess
from flask import Flask, request, session, g, render_template, flash, \
									redirect, url_for
from contextlib import closing
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

app = Flask(__name__)
app.config.from_pyfile('config.cfg') # Initialize app's settings from config.cfg

# Helper function to connect to SQLite3
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# Helper function to init SQLite3 db when app starts
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())

		db.commit()

# Initialize DB connection for each request and tear them down afterwards
@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

# Ping a specific host and report its status
def isAlive(server):
	command = ['ping', '-n', '1', '-w', '1000', server]
	with open(os.devnull, 'w') as DEVNULL:
		res = subprocess.call(command, stdout=DEVNULL, stderr=DEVNULL)
		return res

# Send email when server is down
def sendEmail(serverName):
	body = MIMEText("Server " + serverName + " is down. Please check!", "plain")

	# Get sender and receiver information from config file
	senderUser = app.config['SENDER_USER']
	senderPass = app.config['SENDER_PASS']
	receiver = app.config['RECEIVER']

	email = MIMEMultipart()
	email.attach(body)	

	email["From"] = "Notification"
	email["To"] = "vumaihoan@gmail.com"
	email["Subject"] = "Alert! Server down!!!"

	try:
		# Login to Gmail and send emails using above senders and receivers
		serverSSL = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		serverSSL.ehlo()

		serverSSL.login(senderUser, senderPass)

		# SSL does not support TLS, no need to call serverSSL.starttls()
		serverSSL.sendmail(senderUser, receiver, email.as_string())
		serverSSL.close()
	except:
		print "Error sending email"

############## APP ROUTES ################

# This route is for homepage, always displays all monitored servers
@app.route('/')
def index():
	cur = g.db.execute("select * from servers order by name")
	serverList = [dict(id=row[0], serverName=row[1], status=isAlive(row[1])) for row in cur.fetchall()]
	
	for server in serverList:
		if server['status'] == 1:
			sendEmail(server['serverName'])

	return render_template("index.html", serverList=serverList)

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
	# If method = POST, validate username & password then decide
	error = None
	if request.method == 'POST':
		cur = g.db.execute("select * from users")
		# Get all users and convert the result to a dictionary, otherwise a tuple
		userList = [dict(username=row[0], password=row[1]) for row in cur.fetchall()]
		inputUser = request.form['username']
		inputPass = request.form['password']

		usernameList = [u.get('username') for u in userList]

		if inputUser not in usernameList:
			error = "Username does not exist"
		else:
			for user in userList:
				if user['username'] == inputUser:
					if user['password'] != inputPass:
						error = "Incorrect password"
					else:
						session['logged_in'] = True
						flash('You are logged in')
						return redirect(url_for('index'))

	# If method = GET, simply displays login page
	return render_template('login.html', error=error)

# Logout 
@app.route('/logout')
def logout():
	# Clear the 'logged_in' key to log out
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('index'))

# Add new server to monitor
@app.route('/addServer', methods=['POST'])
def add_server():
	if not session.get('logged_in'):
		abort(401)

	g.db.execute("insert into servers (name) values (?)",
								[request.form['name']])

	g.db.commit()
	return redirect(url_for('index'))

# Remove a server to stop monitoring
@app.route('/removeServer/<serverId>', methods=['POST'])
def remove_server(serverId):
	if not session.get('logged_in'):
		abort(401)

	g.db.execute("delete from servers where id = ?", [serverId])
	g.db.commit()

	return redirect(url_for('index'))

# Viewing/Creating new users
@app.route('/addUser', methods=['GET', 'POST'])
def add_user():
	if not session.get('logged_in'):
		abort(401)

	# If method is GET, display all users
	cur = g.db.execute("select * from users")
	userList = [dict(username=row[0], password=row[1]) for row in cur.fetchall()]
	usernameList = [u.get('username') for u in userList]

	# otherwise, add new user to system
	error = None
	if request.method == 'POST':
		inputUser = request.form['username']
		# If username entered already in the database
		if inputUser in usernameList:
			error = "User already exists!"
		else:	# otherwise, add new user
			g.db.execute("insert into users (username, password) values (?, ?)", 
										[request.form['username'], request.form['password']])

			g.db.commit()
			return redirect(url_for('add_user'))

	return render_template('addUser.html', userList=userList, error=error)

# This route is used to remove an existing user
@app.route('/removeUser/<username>', methods=['POST'])
def remove_user(username):
	if not session.get('logged_in'):
		abort(401)

	g.db.execute("delete from users where username = ?", [username])
	g.db.commit()

	return redirect(url_for('add_user'))

if __name__ == "__main__":
	app.run()
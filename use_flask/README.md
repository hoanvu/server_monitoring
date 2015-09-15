# A simple server monitoring system using Flask

### Overview
+ This system checks all servers it was configured to monitor every 5 seconds and display "Online" or "Offline" status accordingly. 
+ When a server is "Offline", notification email will be sent.

### Functions
This monitoring system has following functions:
+ View all monitored servers and display their status
+ Login / Logout
+ Add new server to monitor*
+ Remove existing server*
+ Add new admin user*
+ Remove existing admin user*
+ Automatically send email when server is "Offline"

> *: those functions only available when user is logged in

### Usage: 
First time see this web app? please run the following commands to init database:
```
$ from server import init_db
$ init_db()
```
Now you are ready to go: <br/>
```
$ python server.py
```
And enjoy, access: http://127.0.0.1:5000

### Configuration
You should change the SENDER_USER, SENDER_PASS and RECEIVER in <strong>config.cfg</strong> for the send/receive email function to work. Notice that you should disable 2-step verification in the SENDER_USER email.

### Need to improve
- Algorithm to check server status is simple, so the app will be slow for many servers
- Password need to be hashed or encrypted before storing to database
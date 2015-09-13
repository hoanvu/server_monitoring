# A simple server monitoring system using Flask

### Usage: 
First time see this web app? please run the following commands to init database: <br/>
```
$ from server import init_db
$ init_db()
```
Now you are ready to go: <br/>
```
$ python server.py
```
And enjoy, access: http://127.0.0.1:5000

### Functions:
- View all monitored servers
- Login / Logout (default user to login: admin/admin)
- Some functions only available when logged in:
   + Add new server to monitor
   + Add new user
   + Remove existing server
   + Remove existing user

### How it works?
- Every 5 seconds, app send 1 ping packet to each server and get the response, then update the status for each server accordingly
- Use jQuery to refresh the server list (the HTML div) every 5 seconds, not refresh the entire page
- Use Bootstrap for frontend decoration
- Bootstrap will be stored locally, not from CDN so when the server is offline, the app still keeps its layout

### Need to improve
- Algorithm to check server status is simple, so the app will be slow for many servers
- Password need to be hashed or encrypted before storing to database
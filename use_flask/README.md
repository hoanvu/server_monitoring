# A simple server monitoring system using Flask

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

### Need to improve
- Algorithm to check server status is simple, so the app will be slow for many servers
- Password need to be hashed or encrypted before storing to database
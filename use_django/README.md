# Simple Server Monitoring System using Django

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

### Configuration
You should change SENDER_EMAIL, SENDER_PASS, RECEIVER_EMAIL settings in <strong>serverMonitor/settings.py</strong> in order to send/receive email function to work. Currently they are not configured. Notice that you should disable 2-step verification in SENDER_EMAIL.

Then in your command prompt (Windows):
```
$ cd use_django
$ set DJANGO_SETTINGS_MODULE = serverMonitor.settings
```
or bash shell (Linux):
```
$ cd use_django
$ set DJANGO_SETTINGS_MODULE = serverMonitor.settings
```

### Usage
```
$ cd use_django
$ python manage.py runserver
```
Now you can start using this application by accessing: http://127.0.0.1:8000/mainApp
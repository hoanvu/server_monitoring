# Simple Server Monitoring System using Django

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
# Simple Server Monitoring System
This repository contains both Flask and Django implementation for this system.

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
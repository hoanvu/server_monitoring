# This file contains extra functions of the system like sending email, check server status

from django.conf import settings
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib, os, subprocess

# Check whether a server is alive using Ping
def isAlive(server):
	command = ['ping', '-n', '1', '-w', '1000', server]
	with open(os.devnull, 'w') as DEVNULL:
		res = subprocess.call(command, stdout=DEVNULL, stderr=DEVNULL)
		return res

# Function to send/receive email
def sendEmail(serverName):
	body = MIMEText("Server " + serverName + " is down. Please check!", "plain")

	# Get sender and receiver information from config file
	senderUser = settings.SENDER_EMAIL
	senderPass = settings.SENDER_PASS
	receiver = settings.RECEIVER_EMAIL

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
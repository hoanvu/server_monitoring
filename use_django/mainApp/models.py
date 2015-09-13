from django.db import models

# Create your models here.
class Server(models.Model):
	servername = models.CharField(max_length=50)
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return self.servername
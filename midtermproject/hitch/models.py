from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 200)
	client_capacity = models.IntegerField(default = 0)
	pricepermile = models.IntegerField(default = 0)
	bag_capacity = models.IntegerField(default = 0)
	departure = models.DateTimeField('date published')
	destination = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.name

class Client(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	pickup = models.CharField(max_length = 50)
	destination = models.CharField(max_length = 50)
	bags = models.IntegerField(default = 0)
	#driver = models.ForeignKey(Driver)
	
	def __unicode__(self):
		return self.name


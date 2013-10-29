from django.db import models

class Driver(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	client_capacity = models.IntegerField(default = 0)
	pricepermile = models.IntegerField(default = 0)
	bag_capacity = models.IntegerField(default = 0)
	departure = models.DateTimeField('date published')
	#def __unicode__(self):
     #   return self.driver_text

class Client(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	pickup = models.CharField(max_length = 50)
	destination = models.CharField(max_length = 50)
	bags = models.IntegerField(default = 0)
	#driver = models.ForeignKey(Driver)
	#def __unicode__(self):  
     #de   return self.client_text


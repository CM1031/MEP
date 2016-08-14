from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	published = models.DateTimeField(blank=True, null=True)
	accepted = models.ForeignKey('auth.User')
	availible = models.PositiveSmallIntegerField()

	def publish(self):
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return self.title

#class User(models.Model):
#	email = models.EmailField(max_length = 254)
#	password = models.CharField(max_length = 64)
#	acct_type = models.PositiveSmallIntegerField()
#	name = models.CharField(max_length = 30)

#	def __str__(self):
#		return self.name

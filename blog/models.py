#database info
from django.db import models

# Create your models here.
class Post(models.Model) :
	title = models.CharField(max_length = 140) #shorter
	body = models.TextField()
	date = models.DateTimeField() #or CharField

	def __str__(self):
		return self.title

#generic views

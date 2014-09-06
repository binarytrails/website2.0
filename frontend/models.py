
from django.db import models
from datetime import date

class Photo(models.Model):
	filename = models.CharField(primary_key = True, 
					max_length = 50)
	title =  models.CharField(max_length = 50)
	author = models.CharField(max_length = 50)
	#date_created = models.DateTimeField('creation date', default = date(1999, 03, 31))
	description = models.CharField(max_length = 250)	

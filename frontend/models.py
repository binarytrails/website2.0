
from django.db import models
from datetime import date

class Photo(models.Model):
	filename = models.CharField( primary_key = True, 
					max_length = 50 )
	title =  models.CharField( max_length = 50,
					blank = False,
					unique = True )
	author = models.CharField( max_length = 50 )
	#date_created = models.DateTimeField( 'creation date', 
	#					default = date(1999, 03, 31) )
	description = models.CharField( max_length = 250 )

class Video(models.Model):
	CATEGORIES = (
		('I', 'Intro'),
		('C', 'Complete'),
		('U', 'Unofficial'),
	)

	filename = models.CharField( primary_key = True,
					max_length = 50 )
	title = models.CharField( max_length = 50,
					blank = False,
					unique = True )
	category = models.CharField( max_length = 1,
					choices = CATEGORIES,
					blank = False )
	author = models.CharField( max_length = 50 )	
	film_director = models.CharField( max_length = 50 )
	sfx_supervisor = models.CharField( max_length = 50 )
	description = models.CharField( max_length = 250 )	

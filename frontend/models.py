from django.db import models
from datetime import date
from django.contrib import admin

class Photo(models.Model):
	filename = models.CharField(
		primary_key = True, 
		max_length = 50
	)
	title =	models.CharField(
		max_length = 50,
		blank = False,
		unique = True
	)
	author = models.CharField(
		max_length = 50
	)
	#date_created = models.DateTimeField( 'creation date', 
	#					default = date(1999, 03, 31) )
	description = models.CharField(
		max_length = 250
	)

class Video(models.Model):
	CATEGORIES = (
		('I', 'Intro'),
		('C', 'Complete'),
		('U', 'Unofficial'),
	)

	filename = models.CharField(
		primary_key = True,
		max_length = 50 
	)
	title = models.CharField(
		max_length = 50,
		blank = False,
		unique = True 
	)
	category = models.CharField(
		max_length = 1,
		choices = CATEGORIES,
		blank = False 
	)
	author = models.CharField(
		max_length = 50
	)
	film_director = models.CharField(
		max_length = 50 
	)
	sfx_supervisor = models.CharField(
		max_length = 50 
	)
	description = models.CharField(
		max_length = 250 
	)

class Skill(models.Model):
	CATEGORIES = (
		('CS', 'Computer science'),
		('DA', 'Digital arts'),
	)
	SUBCATEGORIES = (
		# Computer science
		('MD', 'Methods of development'),
		('OS', 'Operative systems'),
		('F', 'Framework'),
		('RC', 'Revision control'),
		('P', 'Programming'),
		('ML', 'Markup language'),
		('DB', 'Database'),
        ('N', 'Network'),
		('S', 'Server'),
	    ('H', 'Hardware'),
		# Digital arts
		('SE', 'Special effects'),
		('IM', 'Image manipulation')
	)

	title = models.CharField(
		max_length = 10,
		blank = False
	)
	description = models.CharField(
		max_length = 255
	)
	category = models.CharField(
		max_length = 2,
		blank = False,
		choices = CATEGORIES
	)
	subcategory = models.CharField(
		max_length = 2,
		blank = False,
		choices = SUBCATEGORIES
	)
	owner = models.CharField( 
		max_length = 50,
		blank = False 
	)
	rating_on_five = models.DecimalField(
		max_digits = 1,
		decimal_places = 0
	)
	
	# multiple column primary keys are not supported
	class Meta:
		unique_together = ('title', 'owner')


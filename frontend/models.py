from django.db import models

class Photo(models.Model):
	title =  models.CharField(max_length=255)

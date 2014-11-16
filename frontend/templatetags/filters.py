import os
from django import template
from kedfilms import utils

DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
register = template.Library()

@register.filter 
def times(number):
    return range(number)

@register.filter
def in_category(objects, category):
	return objects.filter(category = category)

@register.filter
def imageWidth(path):
	with open(os.path.join(DIR, path), 'rb') as imagefile:
		data = imagefile.read()
		return utils.get_image_info(data)[1]

@register.filter
def imageHeight(path):
	with open(os.path.join(DIR, path), 'rb') as imagefile:
		data = imagefile.read()
		return utils.get_image_info(data)[2]

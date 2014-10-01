"""
Issues:
    Can't return a tuple to template
    Can't use os.path.join() in imageWidth & imageHeight
    Can't return multiple values. rpnMath.
"""

import os
from django import template
from PIL import Image

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
    return Image.open(DIR + str(path)).size[0]

@register.filter
def imageHeight(path):
    return Image.open(DIR + str(path)).size[1]


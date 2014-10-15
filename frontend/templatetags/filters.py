"""
Issues:
    Can't return a tuple to template
        Solution: imageWidth & ImageHeight
    Can't return multiple values
        Solution: rpnMath
"""
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
    return utils.getImageSize(DIR + path)[0]

@register.filter
def imageHeight(path):
    return utils.getImageSize(DIR + path)[1]


from django import template

register = template.Library()

@register.filter 
def times(number):
    return range(number)

@register.filter
def in_subcategory(objects, subcategory):
	return objects.filter(subcategory = subcategory)


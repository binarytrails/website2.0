# Copyright (C) 2014 Vsevolod Ivanov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

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

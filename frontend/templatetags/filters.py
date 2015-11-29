# Copyright (C) 2016 Seva Ivanov
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

register = template.Library()

@register.filter
def times(number): return range(number)

@register.filter 
def fortyfive_times(number): return number * 45

@register.filter
def in_category(objects, category):
    return objects.filter(category = category)

@register.filter
def imageWidth(abspath):
    with open(abspath, 'rb') as imagefile:
        data = imagefile.read()
        return utils.get_image_info(data)[1]

@register.filter
def imageHeight(abspath):
    with open(abspath, 'rb') as imagefile:
        data = imagefile.read()
        return utils.get_image_info(data)[2]

@register.filter
def underscores_to_spaces(text):
    return text.replace("_", " ")

# /projects/ methods
@register.filter
def combine_with_hyphen(first, second):
    return str(first) + "-" + str(second)

@register.filter
def inverse_sign(value):
    return 0 - value

@register.filter
def get_dict_value(dictionary, key):
    return dictionary.get(key)

import calendar
@register.filter
def get_month_name(number):
    return calendar.month_name[number]


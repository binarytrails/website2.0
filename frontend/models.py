"""
* unique constraints are used because multiple primary keys aren't supported.
"""

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

from django.db import models
from datetime import date
from django.contrib import admin

class User(models.Model):
    nick = models.CharField(
        primary_key = True,
        max_length = 50
    )
    name = models.CharField(
        max_length = 50,
        blank = False
    )
    lastname = models.CharField(
        max_length = 50,
        blank = False
    )
    email = models.EmailField(
        blank = False
    )

class Photo(models.Model):
    GN = 'general'
    PF = 'portfolio'
 
    filename = models.CharField(
        primary_key = True,
        max_length = 250
    )
    fragment_identifier = models.CharField(
        max_length = 20,
        unique = True
    )
    title = models.CharField(
        max_length = 50,
        blank = False
    )
    author = models.CharField(
        max_length = 50,
        blank = False
    )
    category = models.CharField(
        max_length = 2,
        blank = False,
        default = GN
    )
    hardware = models.CharField(
        max_length = 50
    )
    application = models.CharField(
        max_length = 50
    )
    date_created = models.DateField(
        default = date.today,
        blank = False
    )    
    owner = models.ForeignKey(
        'User'
    )

    class Meta:
        unique_together = (
            ('owner', 'category', 'title')
        )

class Video(models.Model):
    IN = 'introduction'
    FV = 'favorite'
    EV = 'event'
    DN = 'dancer'

    filename = models.CharField(
        primary_key = True,
        max_length = 250 
    )
    posterfile = models.CharField(
        max_length = 250 
    )
    title = models.CharField(
        max_length = 50,
        blank = False 
    )
    director = models.CharField(
        max_length = 50, 
        blank = False
    )
    description = models.CharField(
        max_length = 50 
    )
    category = models.CharField(
        max_length = 2,
        blank = False
    )
    hardware = models.CharField(
        max_length = 50
    )
    application = models.CharField(
        max_length = 50
    )
    date_created = models.DateField(
        default = date.today,
        blank = False
    )
    owner = models.ForeignKey(
        'User'
    )

    class Meta:
        unique_together = (
            ('owner', 'category', 'title')
        )

class Skill(models.Model):
    GN = "general"
    MD = 'methods of development'
    OS = 'operative system'
    FR = 'framework'
    RC = 'revision control'
    PR = 'programming'
    ML = 'markup language'
    DB = 'database'
    SR = 'server'
    SW = 'sofrware'
    HW = 'hardware'
    VA = 'visual art'

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
        default = GN
    )
    rating_on_five = models.DecimalField(
        max_digits = 1,
        decimal_places = 0
    )
    owner = models.ForeignKey(
        'User'
    )
    
    class Meta:
        unique_together = (
            ('owner' , 'category', 'title')
        )


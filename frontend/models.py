"""
* unique constraints are used because multiple primary keys aren't supported.
"""

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

class Article(models.Model):
    CATEGORIES = (
        ('LX', 'Linux world'),
    )
    SUBCATEGORIES = (
        # Linux World
        ('TM', 'Terminal'),
        ('HW', 'Hardware'),
    )

    title = models.CharField(
        max_length = 50,
        blank = False
    )
    subtitle = models.CharField(
        max_length = 50
    )
    category = models.CharField(
        max_length = 50,
        choices = CATEGORIES,
        blank = False   
    )
    subcategory = models.CharField(
        max_length = 50,
        choices = SUBCATEGORIES,
        blank = False
    )
    date_created = models.DateField(
        default = date.today
    )
    date_modified = models.DateField(
        default = date.today
    )
    author = models.ForeignKey(
        'User'
    )

    class Meta:
        unique_together = (
            ('author', 'title', 'category', 'subcategory')
        )

class Photo(models.Model):
    CATEGORIES = (
        ('GN', 'General'),
        ('PF', 'Portfolio'),
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
    description = models.CharField(
        max_length = 250
    )
    category = models.CharField(
        max_length = 2,
        choices = CATEGORIES,
        blank = False 
    )
    author = models.CharField(
            max_length = 50,
            blank = False
        )
    date_created = models.DateField(
        default = date.today
    )    
    owner = models.ForeignKey(
        'User'
    )

    class Meta:
        unique_together = (
            ('owner', 'title', 'category')
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
    description = models.CharField(
        max_length = 250 
    )
    category = models.CharField(
        max_length = 2,
        choices = CATEGORIES,
        blank = False 
    )
    author = models.CharField(
        max_length = 50,
        blank = False
    )
    director = models.CharField(
        max_length = 50 
    )
    sfx = models.CharField(
        max_length = 50 
    )
    owner = models.ForeignKey(
        'User'
    )

    class Meta:
        unique_together = (
            ('owner', 'title', 'category')
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
        ('IM', 'Image manipulation'),
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
    rating_on_five = models.DecimalField(
        max_digits = 1,
        decimal_places = 0
    )
    owner = models.ForeignKey(
        'User'
    )
    
    class Meta:
        unique_together = (
            ('owner', 'title', 'category', 'subcategory')
        )


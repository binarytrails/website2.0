# Copyright (C) 2015 Vsevolod Ivanov
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

"""
    unique constraints are used because multiple primary keys aren't supported.
"""

import pyexiv2
import os, shutil, imghdr
from datetime import date

from kedfilms import utils

from django.db import models
from django.contrib import admin
from django.conf import settings
from django.core.exceptions import ValidationError

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MEDIA_URL = settings.MEDIA_URL
IMAGES_ROOT = os.path.join(settings.MEDIA_ROOT, "images")
IMAGES_DIRNAME = "original"
THUMBNAILS_DIRNAMES = ['x200', 'x800']

# offline uploads only, hence, no media/ used.
def get_photo_upload_to_by_category(instance, filename):
    return os.path.join("images", instance.category, "original", filename)

class Photo(models.Model):
    def __unicode__(self):
        return self.title

    # Add new categories here
    PORTFOLIO = 'portfolio'
    DAYTIME = 'daytime'
    NIGHTTIME = 'nighttime'
    MULTIVERSE = 'multiverse'
    INTERNET_GIFS = 'internet_in_motion'
    CATEGORIES = (
        (PORTFOLIO, 'Portfolio'),
        (DAYTIME, 'Daytime'),
        (NIGHTTIME, 'Nighttime'),
        (MULTIVERSE, 'Multiverse'),
        (INTERNET_GIFS, 'Internet In Motion'),
    )

    # Add new authors here
    SEVA = 'Vsevolod Ivanov'
    MELO = 'Melodie Verroeulst'
    ANDREI = 'Andrei Savin'
    SAND = 'Sandrine Allen'
    GUIDES = 'Guillaume Deshaies'
    INTERNET = 'Internet'
    AUTHORS = (
        (SEVA, 'Vsevolod Ivanov'),
        (MELO, 'Melodie Verroeulst'),
        (ANDREI, 'Andrei Savin'),
        (SAND, 'Sandrine Allen'),
        (GUIDES, 'Guillaume Deshaies'),
        (INTERNET, 'Internet'),
    )

    # Add new hardware here
    CANON = 'Canon EOS REBEL T3i'
    IPHONE = 'Iphone'
    HARDWARES = (
        (CANON, 'Canon EOS REBEL T3i'),
        (IPHONE, 'Iphone')
    )

    # Add new software here
    AE = 'Adobe After Effect'
    GIMP28 = 'Gimp 2.8'
    APPLICATIONS = (
        (AE, 'Adobe After Effect'),
        (GIMP28, 'Gimp 2.8')
    )

    category = models.CharField(
        max_length = 20,
        blank = False,
        choices = CATEGORIES,
        default = PORTFOLIO
    )
    cached_category = models.CharField(
        max_length = 200,
        blank = True
    )
    image = models.ImageField(
        blank = False,
        upload_to = get_photo_upload_to_by_category
    )
    cached_image_path = models.CharField(
        max_length = 200,
        unique = True,
        blank = True
    )
    fragment_identifier = models.CharField(
        max_length = 41,
        unique = True
    )
    title = models.CharField(
        max_length = 50,
        blank = False
    )
    author = models.CharField(
        max_length = 50,
        blank = False,
        choices = AUTHORS,
        default = SEVA
    )
    hardware = models.CharField(
        max_length = 50,
        blank = True,
        choices = HARDWARES
    )
    application = models.CharField(
        max_length = 50,
        blank = True,
        choices = APPLICATIONS
    )
    date_created = models.DateField(
        default = date.today,
        blank = False
    )

    def get_category_tuple(self, category = None):
        if category == None:
            category = self.category

        for key, value in self.CATEGORIES:
            if key == category:
                return (key, value)

    def get_next_category(self, category):
        length = len(self.CATEGORIES) - 1

        for key, value in self.CATEGORIES:
            if key == category:
                index = self.CATEGORIES.index((key, value))

                if index < length:
                    return self.CATEGORIES[index + 1]
                else:
                    return self.CATEGORIES[0]

    def get_previous_category(self, category):
        length = len(self.CATEGORIES) - 1

        for key, value in self.CATEGORIES:
            if key == category:
                index = self.CATEGORIES.index((key, value))

                if index > 0:
                    return self.CATEGORIES[index - 1]
                else:
                    return self.CATEGORIES[length]  

    def get_image_url(self):
        return os.path.join(MEDIA_URL, "images", self.category, IMAGES_DIRNAME, 
            os.path.basename(str(self.image))
        )

    def get_image_thumbnails_urls(self):
        urls = {}
        for dirname in THUMBNAILS_DIRNAMES:
            urls[dirname] = os.path.join(MEDIA_URL, "images", self.category, 
                dirname, os.path.basename(str(self.image))
            )
        return urls

    def get_image_abspath(self):
        return os.path.join(IMAGES_ROOT, self.category, IMAGES_DIRNAME, 
            os.path.basename(str(self.image))
        )

    @property
    def get_image_type(self):
        return imghdr.what(self.get_image_abspath())

    def get_image_thumbnails_abspaths(self):
        abspaths = {}
        for dirname in THUMBNAILS_DIRNAMES:
            abspaths[dirname] = os.path.join(IMAGES_ROOT, self.category,
                dirname, os.path.basename(str(self.image))
            )
        return abspaths

    def get_thumbnails_abspaths(self):
        filename = os.path.basename(self.cached_image_path)
        thumbnails_abspaths = []

        for dirname in THUMBNAILS_DIRNAMES:
            thumbnail_path = os.path.join(IMAGES_ROOT, self.category, dirname, filename)
            thumbnails_abspaths.append(thumbnail_path)

        return thumbnails_abspaths

    # each metadata key is associated with a photo attribute
    def get_image_xmp_metadata_available_keys(self):
        return ["Xmp.xmp.title", "Xmp.xmp.fragment_identifier",
            "Xmp.xmp.author", "Xmp.xmp.date_created", "Xmp.xmp.application",
            "Xmp.xmp.hardware"
        ]

    def get_image_xmp_metadata(self):
        metadata = pyexiv2.ImageMetadata(self.cached_image_path)
        metadata.read()

        available_metadata = {}
        available_keys = self.get_image_xmp_metadata_available_keys()

        for key in available_keys:
            available_metadata[key] = metadata[key].value

        return available_metadata

    # convert is ImageMagick
    def generate_thumbnails(self, is_gif=False):
        filename = os.path.basename(self.cached_image_path)
        source = self.cached_image_path

        for dirname in THUMBNAILS_DIRNAMES:
            if is_gif and dirname != 'x200': continue

            new_size = dirname
            thumbnail_path = os.path.join(IMAGES_ROOT, self.category, dirname)

            if is_gif:
                target = os.path.join(thumbnail_path, "temporary-" + filename)
                os.system("convert " + source + " -coalesce " + target)
                source = target
            
            target = os.path.join(thumbnail_path, filename)
            os.system("convert " + source + " -resize " + new_size + " " + target)

            if is_gif and os.path.exists(source):
                    os.remove(source)

    def generate_image_xmp_metadata(self):
        metadata = pyexiv2.ImageMetadata(self.cached_image_path)
        metadata.read()

        for key in self.get_image_xmp_metadata_available_keys():
            attribute = key.replace('Xmp.xmp.', '')
            value = self.__dict__.get(attribute)
            if type(value) == date:
                value = str(value)
            metadata[key] = value

        metadata.write()

    def move_image_to_updated_category(self):
        filename = os.path.basename(self.cached_image_path)
        subdirectories = THUMBNAILS_DIRNAMES + [IMAGES_DIRNAME]

        for subdirectory in subdirectories:
            current_image_path = os.path.join(IMAGES_ROOT, self.cached_category, subdirectory, filename)
            new_image_path = os.path.join(IMAGES_ROOT, self.category, subdirectory, filename)

            # destination has this file
            if os.path.isfile(new_image_path):
                raise ValidationError("Can't change the image category: Same image filename exists.")

            shutil.move(current_image_path, new_image_path)

    def delete_image(self):
        if os.path.exists(self.cached_image_path):
            os.remove(self.cached_image_path)

    def delete_thumbnails(self):
        filename = os.path.basename(self.cached_image_path)

        for dirname in THUMBNAILS_DIRNAMES:
            thumbnail_path = os.path.join(IMAGES_ROOT, self.category, dirname, filename)

            if os.path.exists(thumbnail_path):
                os.remove(thumbnail_path)

    # overwritten method
    def delete(self, *args, **kwargs):
        super(Photo, self).delete(*args, **kwargs)
        self.delete_image()
        self.delete_thumbnails()

    class Meta:
        unique_together = (
            ('category', 'fragment_identifier')
        )

class Video(models.Model):
    INTRO = 'intro'
    FAVORITE = 'favorite'
    EVENT = 'event'
    DANCER = 'dancer'

    CATEGORIES = (
        (INTRO, 'Brief introductory passage'),
        (FAVORITE, 'Personal Favorites'),
        (EVENT, 'A Gathering Of People'),
        (DANCER, 'Physical Expression'),
    )

    category = models.CharField(
        max_length = 2,
        blank = False,
        choices = CATEGORIES
    )
    date_created = models.DateField(
        default = date.today,
        blank = False
    )
    # blank = video locally hosted
    iframe_src = models.CharField(
        max_length = 250,
        unique = True,
        blank = True
    )
    # locally hosted video information
    filename = models.CharField(
        max_length = 250
    )
    posterfile = models.CharField(
        max_length = 250 
    )
    title = models.CharField(
        max_length = 50
    )
    author = models.CharField(
        max_length = 50
    )
    description = models.CharField(
        max_length = 50 
    )
    hardware = models.CharField(
        max_length = 50
    )
    application = models.CharField(
        max_length = 50
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
    
    class Meta:
        unique_together = (
            ('category', 'title')
        )

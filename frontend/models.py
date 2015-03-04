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

import os, shutil, pyexiv2
from datetime import date

from django.db import models
from django.contrib import admin
from django.conf import settings
from django.core.exceptions import ValidationError

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MEDIA_URL = settings.MEDIA_URL
IMAGES_ROOT = os.path.join(settings.MEDIA_ROOT, "images")
IMAGES_DIRNAME = "original"
THUMBS_DIRNAMES = ['x200', 'x800']

# offline uploads only, hence, no media/ used.
def get_photo_upload_to_by_category(instance, filename):
    return os.path.join("images", instance.category, "original", filename)

class Photo(models.Model):
    def __unicode__(self):
        return self.title

    # Add new categories here
    GENERAL = 'general'
    PORTFOLIO = 'portfolio'
    CATEGORIES = (
        (GENERAL, 'General'),
        (PORTFOLIO, 'Portfolio'),
    )

    category = models.CharField(
        max_length = 10,
        blank = False,
        choices = CATEGORIES,
        default = GENERAL
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
        max_length = 20
    )
    title = models.CharField(
        max_length = 50,
        blank = False
    )
    author = models.CharField(
        max_length = 50,
        blank = False
    )
    hardware = models.CharField(
        max_length = 50,
        blank = True
    )
    application = models.CharField(
        max_length = 50,
        blank = True
    )
    date_created = models.DateField(
        default = date.today,
        blank = False
    )

    def get_image_url(self):
        return os.path.join(MEDIA_URL, "images", self.category, IMAGES_DIRNAME, 
            os.path.basename(str(self.image))
        )

    def get_image_abspath(self):
        return os.path.join(IMAGES_ROOT, self.category, IMAGES_DIRNAME, 
            os.path.basename(str(self.image))
        )

    def get_thumbnails_abspaths(self):
        filename = os.path.basename(self.cached_image_path)
        thumbnails_abspaths = []

        for thumb_dirname in THUMBS_DIRNAMES:
            thumbnail_path = os.path.join(IMAGES_ROOT, self.category, thumb_dirname, filename)
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

    def generate_thumbnails(self):
        filename = os.path.basename(self.cached_image_path)

        for thumb_dirname in THUMBS_DIRNAMES:
            thumbnail_path = os.path.join(IMAGES_ROOT, self.category, thumb_dirname, filename)

            # ImageMagick; New thumb size is also its directory name
            os.system("convert " + self.cached_image_path + " -resize " + 
                thumb_dirname + " " + thumbnail_path
            )

    def generate_image_xmp_metadata(self):
        metadata = pyexiv2.ImageMetadata(self.cached_image_path)
        metadata.read()

        for key in self.get_image_xmp_metadata_available_keys():
            attribute = key.replace('Xmp.xmp.', '')
            metadata[key] = str(self.__dict__.get(attribute))

        metadata.write()

    def move_image_to_updated_category(self):
        filename = os.path.basename(self.cached_image_path)
        subdirectories = THUMBS_DIRNAMES + [IMAGES_DIRNAME]

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

        for thumb_dirname in THUMBS_DIRNAMES:
            thumbnail_path = os.path.join(IMAGES_ROOT, self.category, thumb_dirname, filename)

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

    class Meta:
        unique_together = (
            ('category', 'title')
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

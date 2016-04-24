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

"""
    unique constraints are used because multiple primary keys aren't supported.
    import_export:
        import:
            using primary_key will create KeyError: u'id'.
            w/o null=True -> 'NOT NULL constraint failed' on empty fields.
"""

import os, shutil, imghdr
from datetime import date

from kedfilms import utils

from django.db import models
from django.contrib import admin
from django.conf import settings
from django.core.exceptions import ValidationError

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MEDIA_URL = settings.MEDIA_URL
MEDIA_ROOT = settings.MEDIA_ROOT
IMAGES_ROOT = os.path.join(MEDIA_ROOT, "images")
IMAGES_DIRNAME = "original"
THUMBNAILS_DIRNAMES = ["x200", "x800"]

def photo_upload_to(instance, filename):
    return os.path.join(MEDIA_ROOT, "images",
        instance.category.folder, "original", filename)

def article_upload_to(instance, filename):
    return os.path.join(MEDIA_ROOT, "articles",
        instance.category.folder, filename)

class Author(models.Model):
    name = models.CharField(
        unique = True,
        max_length = 50,
        default = "Unknown"
    )
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length = 50,
    )
    context = models.CharField(
        max_length = 50
    )
    folder = models.CharField(
        max_length = 50,
        blank = True,
        null=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = (
            ("name", "context")
        )

class Article(models.Model):
    author = models.ForeignKey("Author")
    category = models.ForeignKey(
        "Category",
        limit_choices_to={"context": "Article"}
    )
    title = models.CharField(
        unique = True,
        max_length = 50
    )
    content = models.TextField(
        max_length = 40000
    )
    file = models.FileField(
        max_length = 200,
        upload_to = article_upload_to,
        null = True
    )
    url = models.URLField(
        max_length = 200,
        blank = True,
        null = True
    )
    creation_date = models.DateField(
        default = date.today
    )

class Photo(models.Model):
    author = models.ForeignKey("Author")
    category = models.ForeignKey(
        "Category",
        limit_choices_to={"context": "Photo"}
    )
    cached_category = models.ForeignKey(
        "Category",
        related_name="cached_category",
        limit_choices_to={"context": "Photo"}
    )
    hardware = models.ForeignKey(
        "Category",
        related_name="hardware",
        limit_choices_to={"context": "Hardware"},
        blank = True,
        null = True
    )
    application = models.ForeignKey(
        "Category",
        related_name="application",
        limit_choices_to={"context": "Software"},
        blank = True,
        null = True
    )
    image = models.ImageField(
        max_length = 200,
        upload_to = photo_upload_to
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
        max_length = 50
    )
    creation_date = models.DateField(
        default = date.today
    )

    @property
    def get_image_type(self):
        return imghdr.what(self.get_image_abspath())

    def get_image_url(self):
        return os.path.join(MEDIA_URL, "images", self.category.folder, IMAGES_DIRNAME, 
            os.path.basename(str(self.image))
        )

    def get_image_thumbnails_urls(self):
        urls = {}
        for dirname in THUMBNAILS_DIRNAMES:
            urls[dirname] = os.path.join(MEDIA_URL, "images", self.category.folder, 
                dirname, os.path.basename(str(self.image))
            )
        return urls

    def get_image_abspath(self):
        return os.path.join(IMAGES_ROOT, self.category.folder, IMAGES_DIRNAME, 
            os.path.basename(str(self.image))
        )

    def get_image_thumbnails_abspaths(self):
        # used in views as dict, TODO: remove duplicate
        abspaths = {}
        for dirname in THUMBNAILS_DIRNAMES:
            abspaths[dirname] = os.path.join(IMAGES_ROOT, self.category.folder,
                dirname, os.path.basename(str(self.image))
            )
        return abspaths

    def get_thumbnails_abspaths(self):
        filename = os.path.basename(self.cached_image_path)
        thumbnails_abspaths = []

        for dirname in THUMBNAILS_DIRNAMES:
            thumbnail_path = os.path.join(IMAGES_ROOT, 
                self.category.folder, dirname, filename
            )
            thumbnails_abspaths.append(thumbnail_path)

        return thumbnails_abspaths

    def generate_thumbnails(self, is_gif=False):
        """convert is part of ImageMagick"""
        filename = os.path.basename(self.cached_image_path)
        source = self.cached_image_path

        for dirname in THUMBNAILS_DIRNAMES:
            new_size = dirname
            thumbnail_path = os.path.join(IMAGES_ROOT, self.category.folder, dirname)

            if os.path.exists(thumbnail_path) == False:
                os.makedirs(thumbnail_path)

            if is_gif and dirname != "x200":
                continue
            elif is_gif:
                target = os.path.join(thumbnail_path, "temporary-" + filename)
                os.system("convert " + source + " -coalesce " + target)
                source = target
            
            target = os.path.join(thumbnail_path, filename)
            os.system("convert " + source + " -resize " + new_size + " " + target)

            if is_gif and os.path.exists(source):
                os.remove(source)

    def move_image_to_updated_category(self):
        filename = os.path.basename(self.cached_image_path)
        subdirectories = THUMBNAILS_DIRNAMES + [IMAGES_DIRNAME]

        for subdirectory in subdirectories:
            current_image_path = os.path.join(IMAGES_ROOT,
                self.cached_category.folder, subdirectory, filename
            )
            new_image_path = os.path.join(IMAGES_ROOT, 
                self.category.folder, subdirectory, filename
            )
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
            thumbnail_path = os.path.join(IMAGES_ROOT, self.category.folder, dirname)
            if os.path.exists(thumbnail_path):
                shutil.rmtree(thumbnail_path)

    def delete(self, *args, **kwargs):
        """overwritten method"""
        super(Photo, self).delete(*args, **kwargs)
        self.delete_image()
        self.delete_thumbnails()

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = (
            ("category", "fragment_identifier")
        )

class Video(models.Model):
    iframe_src = models.CharField(
        max_length = 250,
        unique = True
    )
    creation_date = models.DateField(
        default = date.today
    )
    category = models.ForeignKey(
        "Category",
        limit_choices_to={"context": "Video"}
    )

class Project(models.Model):
    title = models.CharField(
        unique = True,
        max_length = 50
    )
    description = models.TextField(
        max_length = 500
    )
    url = models.CharField(
        unique = True,
        max_length = 80
    )
    creation_date = models.DateField(
        default = date.today
    )

class Update(models.Model):
    title = models.CharField(
        unique = True,
        max_length = 50
    )
    url = models.CharField(
        unique = True,
        max_length = 80
    )
    creation_date = models.DateField(
        default = date.today
    )


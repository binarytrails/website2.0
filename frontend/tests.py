# coding=utf-8

# Copyright (C) 2016 Seva Ivanov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU GENERAL Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU GENERAL Public License for more details.
#
# You should have received a copy of the GNU GENERAL Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os, shutil
import pyexiv2
from datetime import date

from kedfilms import utils

from django.test import TestCase
from django.core.files import File
from django.contrib.admin.sites import AdminSite

from frontend.models import Author, Category, Photo
from frontend.models import IMAGES_ROOT
from frontend.admin import PhotoAdmin

DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(DIR, "test-data")

class PhotoAdminTests(TestCase):
    """
        TODO:
            Image Update
            Create new image to avoid messing with directories
    """
    def setUp(self):
        self.author = Author.objects.create(
            name = "Unknown"
        )
        self.category_test = Category.objects.create(
            name = "test",
            context = "Photo"
        )
        self.category_test2 = Category.objects.create(
            name = "test2",
            context = "Photo"
        )
        self.category_hardware = Category.objects.create(
            name = "Camera",
            context = "Hardware"
        )
        self.category_software = Category.objects.create(
            name = "Life Invader",
            context = "Software"
        )
        self.photo = Photo.objects.create(
            category = self.category_test,
            cached_category = self.category_test,
            image = "",
            cached_image_path = "",
            fragment_identifier = "horse",
            title = "Weird Horse",
            author = self.author,
            hardware = self.category_hardware,
            application = self.category_software,
            date_created = date(1965, 1, 1)
        )
        image1 = File(open(os.path.join(TEST_DIR, "horse.jpg")))
        self.photo.image.save("horse.jpg", image1, True)

#        self.photo2 = Photo.objects.create(
#            category = self.category_test,
#            cached_category = self.category_test2,
#            image = "",
#            cached_image_path = "",
#            fragment_identifier = "hipster",
#            title = "Hipster Cat",
#            author = self.author,
#            hardware = self.category_hardware,
#            application = self.category_software,
#            date_created = date(1956, 1, 1)
#        )
#        image2 = File(open(os.path.join(TEST_DIR, "hipster.jpg")))
#        self.photo2.image.save("hipster.jpg", image2, True)

        self.site = AdminSite()
        self.photoAdmin = PhotoAdmin(Photo, self.site)

        # Make photos with args : request, object, form, change
        self.photoAdmin.save_model(None, self.photo, None, True)
        #self.photoAdmin.save_model(None, self.photo2, None, True)

        self.thumbnails = self.photo.get_thumbnails_abspaths()

    def tearDown(self):
        self.photo.delete()
        #self.photo2.delete()

    def test_create_and_upload(self):
        # Asserts
        self.assertEqual(self.photo.category, self.category_test)
        self.assertEqual(self.photo.category, self.photo.cached_category)

        self.assertTrue(os.path.exists(self.photo.cached_image_path))
        for thumbnail in self.thumbnails:
            self.assertTrue(os.path.exists(thumbnail))

    def test_create_with_unicode_title_containing_an_accent(self):
        # Arrange
        title = u"Béate"
        self.photo.title = title

        # Acts
        self.photoAdmin.save_model(None, self.photo, None, True)

        # Asserts
        self.assertEqual(title, self.photo.title)

    def test_correct_image_width_and_height(self):
        # Arrange
        width = 0
        height = 0
        with open(self.photo.cached_image_path, 'rb') as imagefile:
            data = imagefile.read()
            image_info = utils.get_image_info(data)
            width = image_info[1]
            height = image_info[2]

        # Asserts
        self.assertEqual(self.photo.image.width, width)
        self.assertEqual(self.photo.image.height, height)

    def test_change_category_of_image_with_available_filename_at_destination(self):
        # Arrange
        self.photo.category = self.category_test2

        # Acts
        self.photoAdmin.save_model(None, self.photo, None, True)
        self.thumbnails = self.photo.get_thumbnails_abspaths()

        # Asserts
        self.assertEqual(self.photo.category, self.category_test2)
        self.assertEqual(self.photo.category, self.photo.cached_category)

        self.assertTrue(os.path.exists(self.photo.cached_image_path))
        for thumbnail in self.thumbnails:
            self.assertTrue(os.path.exists(thumbnail))

    def test_change_category_of_image_with_non_available_filename_at_destination(self):
        # uniques cached_image_path prevents
        pass

    def test_delete_image_and_thumbnails(self):
        # Acts
        self.photo.delete_image()
        self.photo.delete_thumbnails()

        # Asserts
        self.assertFalse(os.path.exists(self.photo.image.path))
        for thumbnail in self.thumbnails:
            self.assertFalse(os.path.exists(thumbnail))


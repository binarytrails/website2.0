# Copyright (C) 2015 Vsevolod Ivanov
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

import os, pyexiv2
from datetime import date

from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from django.core.files import File

from frontend.models import Photo
from frontend.admin import PhotoAdmin

DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(DIR, "test-data")

class PhotoAdminTests(TestCase):
    # Test cases:
    #       + Create
    #       + Category Update
    #       + Image Update
    #       + Metadata Update
    #       - Category & Image Updates
    #       - Alert on same image filename on category change
    #       + Delete

    def setUp(self):
        self.photo = Photo.objects.create(
            category = Photo.GENERAL,
            cached_category = "",
            image = "",
            cached_image_path = "",
            fragment_identifier = "horse",
            title = "Awesome Horse",
            author = "Internet",
            hardware = "Camera",
            application = "Instagram",
            date_created = date(1965, 1, 1)
        )
        imagename = "horse.jpg"
        imagefile = File(open(os.path.join(TEST_DIR, imagename)))
        self.photo.image.save(imagename, imagefile, True)
        self.thumbnails = []

        self.site = AdminSite()
        self.photoAdmin = PhotoAdmin(Photo, self.site)

        # Creates Photo: params: request, object, form, change
        self.photoAdmin.save_model(None, self.photo, None, True)
        self.thumbnails = self.photo.get_thumbnails_abspaths()

    def tearDown(self):
        self.photo.delete_image()
        self.photo.delete_thumbnails()

    def test_create_and_upload(self):
        # Asserts
        self.assertEqual(self.photo.category, Photo.GENERAL)
        self.assertEqual(self.photo.category, self.photo.cached_category)

        self.assertTrue(os.path.exists(self.photo.cached_image_path))
        for thumbnail in self.thumbnails:
            self.assertTrue(os.path.exists(thumbnail))

    def test_add_image_xmp_metadata(self):
        # Acts
        metadata = pyexiv2.ImageMetadata(self.photo.cached_image_path)
        metadata.read()

        # Assert
        self.assertEqual(metadata["Xmp.xmp.title"].value, self.photo.title)
        self.assertEqual(metadata["Xmp.xmp.fragment_identifier"].value, self.photo.fragment_identifier)
        self.assertEqual(metadata["Xmp.xmp.author"].value, self.photo.author)
        self.assertEqual(metadata["Xmp.xmp.date_created"].value, str(self.photo.date_created))
        self.assertEqual(metadata["Xmp.xmp.application"].value, self.photo.application)
        self.assertEqual(metadata["Xmp.xmp.hardware"].value, self.photo.hardware)

    def test_change_category_of_image_with_available_filename_at_destination(self):
        # Arrange
        self.photo.category = Photo.PORTFOLIO

        # Acts
        self.photoAdmin.save_model(None, self.photo, None, True)
        self.thumbnails = self.photo.get_thumbnails_abspaths()

        # Asserts
        self.assertEqual(self.photo.category, Photo.PORTFOLIO)
        self.assertEqual(self.photo.category, self.photo.cached_category)

        self.assertTrue(os.path.exists(self.photo.cached_image_path))
        for thumbnail in self.thumbnails:
            self.assertTrue(os.path.exists(thumbnail))


    def test_change_category_of_image_with_non_available_filename_at_destination(self):
        # Arrange

        # Acts

        # Asserts
        pass

    def test_delete_image_and_thumbnails(self):
        # Acts
        self.photo.delete_image()
        self.photo.delete_thumbnails()

        # Asserts
        self.assertFalse(os.path.exists(self.photo.image.path))
        for thumbnail in self.thumbnails:
            self.assertFalse(os.path.exists(thumbnail))

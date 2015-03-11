# coding=utf-8
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

from kedfilms import utils

from django.test import TestCase
from django.core.files import File
from django.contrib.admin.sites import AdminSite

from frontend.models import Photo
from frontend.admin import PhotoAdmin

DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(DIR, "test-data")

class PhotoAdminTests(TestCase):
    # Main functionalities:
    #       + Create
    #       + Category Update
    #       + Image Update
    #       + Metadata Update
    #       - Category & Image Updates
    #       - Alert on same image filename on category change
    #       + Delete

    def setUp(self):
        self.photo = Photo.objects.create(
            category = Photo.CATEGORIES[0][0],
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
        self.photo.delete()

    def test_create_and_upload(self):
        # Asserts
        self.assertEqual(self.photo.category, Photo.CATEGORIES[0][0])
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

    def test_xmp_metadata_was_added_correctly_to_the_imagefile_on_creation(self):
        # Acts
        metadata = pyexiv2.ImageMetadata(self.photo.cached_image_path)
        metadata.read()

        # Assert
        for key in self.photo.get_image_xmp_metadata_available_keys():
            attribute = key.replace('Xmp.xmp.', '')
            value = self.photo.__dict__.get(attribute)
            if type(value) == date:
                value = str(value)
            # comparing metadata values with associated photo attributes values
            self.assertEqual(metadata[key].value, value)

    def test_get_xmp_metadata_from_model(self):
        # Acts
        metadata = self.photo.get_image_xmp_metadata()

        # Assert
        for key in self.photo.get_image_xmp_metadata_available_keys():
            attribute = key.replace('Xmp.xmp.', '')
            value = self.photo.__dict__.get(attribute)
            if type(value) == date:
                value = str(value)
            # comparing metadata values with associated photo attributes values
            self.assertEqual(metadata.get(key), value)

    def test_get_next_category_before_last_index_returns_next(self):
        # Arrange
        category_tuple = self.photo.get_category_tuple()
        next_index = self.photo.CATEGORIES.index(category_tuple) + 1

        # Acts
        next_category = self.photo.get_next_category(self.photo.category)

        # Asserts
        self.assertEqual(next_category, self.photo.CATEGORIES[next_index])

    def test_get_next_category_at_last_index_returns_first(self):
        # Arrange
        last_index = len(self.photo.CATEGORIES) - 1
        category = self.photo.CATEGORIES[last_index][0]

        # Acts
        next_category = self.photo.get_next_category(category)

        # Asserts
        self.assertEqual(next_category, self.photo.CATEGORIES[0])

    def test_get_previous_category_before_first_index_returns_previous(self):
        # Arrange
        second_category = self.photo.CATEGORIES[1][0]

        # Acts
        previous_category = self.photo.get_previous_category(second_category)

        # Asserts
        self.assertEqual(previous_category, self.photo.CATEGORIES[0])

    def test_get_previous_category_at_first_index_returns_last(self):
        # Arrange
        first_category = self.photo.CATEGORIES[0][0]

        last_index = len(self.photo.CATEGORIES) - 1
        last_category = self.photo.CATEGORIES[last_index]

        # Acts
        previous_category = self.photo.get_previous_category(first_category)

        # Asserts
        self.assertEqual(previous_category, last_category)

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
        self.photo.category = Photo.CATEGORIES[1][0]

        # Acts
        self.photoAdmin.save_model(None, self.photo, None, True)
        self.thumbnails = self.photo.get_thumbnails_abspaths()

        # Asserts
        self.assertEqual(self.photo.category, Photo.CATEGORIES[1][0])
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

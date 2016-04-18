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

import imghdr, uuid
from datetime import date

from django.contrib import admin
from django.contrib import messages
from django.db import IntegrityError

from django.shortcuts import render_to_response

from django.conf.urls import patterns, url
from django.http import HttpResponseRedirect
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.views.decorators import staff_member_required

from frontend.models import Author, Category, Photo, Video

# Describes how this resource can be imported or exported
from import_export import resources
# django.contrib admin.ModelAdmin wrapper
from import_export.admin import ImportExportModelAdmin

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin):
    pass

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Author

class CategoryAdmin(ImportExportModelAdmin):
    # Select Form
    list_display = ['id', 'name', 'folder', 'context']

class PhotoResource(resources.ModelResource):
    class Meta:
        model = Photo

from import_export.admin import ImportExportModelAdmin

class PhotoAdmin(ImportExportModelAdmin):
    # Select Form
    list_display = ['title', 'fragment_identifier', 'category', 
        'date_created', 'application', 'hardware', 'author'
    ]
    search_fields = ['title']
    readonly_fields = ['cached_image_path']

    # Edit form
    fields = [
        'category',
        'image',
        'cached_image_path',
        'fragment_identifier',
        'title', 
        'author',
        'hardware',
        'application',
        'date_created'
    ]

    def save_model(self, request, object, form, change):
        """
            TODO:
                Simplify with action type
                Bulk delete -> call delete() for all items
                Updating gifs
        """
        make_thumbnails = False

        # first image upload
        if not object.cached_image_path:
            make_thumbnails = True

        # category update
        elif object.cached_category != object.category:
            make_thumbnails = False
            object.move_image_to_updated_category()
            # can't do it on creation: 404 Bad Request
            object.image.name = object.get_image_url()

        # image update
        elif object.cached_image_path != object.get_image_abspath():
            make_thumbnails = True
            object.delete_image()
            object.delete_thumbnails()

        object.cached_category = object.category
        object.cached_image_path = object.get_image_abspath()

        # image upload & records updates
        object.save()

        is_gif = False
        if imghdr.what(object.cached_image_path) == "gif":
            is_gif = True
        
        if make_thumbnails:
            object.generate_thumbnails(is_gif)

class VideoResource(resources.ModelResource):
    class Meta:
        model = Author

class VideoAdmin(ImportExportModelAdmin):
    # Select Form
    list_display = ['id', 'iframe_src', 'date_created', 'category']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)

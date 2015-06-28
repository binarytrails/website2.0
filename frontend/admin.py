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
    The admin panel is for developing only.
"""

import pyexiv2
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

from frontend.models import Photo

@staff_member_required
def import_photos(request):
    if request.method == 'POST':
        # load images to upload in memory
        photos_files = request.FILES.getlist('photos')
        photoAdmin = PhotoAdmin(Photo, AdminSite())

        for photo_file in photos_files:
            photo = Photo()
            filename = photo_file.name
            photo.category = request.POST['category']

            if imghdr.what(photo_file.name, photo_file.read()) == "gif":
                photo_uuid = str(uuid.uuid1())
                filename = photo_uuid + ".gif"

                photo.title = filename
                photo.fragment_identifier = photo_uuid
                photo.author = Photo.INTERNET

            else:
                # read uploaded image metadata
                metadata = pyexiv2.ImageMetadata.from_buffer(photo_file.read())
                metadata.read()

                # verify xmp metadata
                for key in photo.get_image_xmp_metadata_available_keys():
                    # save image metadata into created photo matching attributes
                    attribute = key.replace('Xmp.xmp.', '')
                    try:
                        photo.__dict__[attribute] = metadata[key].value
                    except KeyError as error:
                        messages.error(request, "Xmp metadata key '%s' not found!" % key)
                        break

            # save image to the photo object
            try:
                photo.image.save(filename, photo_file, True)
            except IntegrityError as error:
                messages.error(request, error.args)
                break

            # run the save_model used for creating/modifing a photo object
            photoAdmin.save_model(None, photo, None, True)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])

"""
    Not implemented:
        Updating gifs.
        Bulk delete won't call delete() for all the items.
"""
class PhotoAdmin(admin.ModelAdmin):
    # Select Form
    list_display = ['title', 'fragment_identifier', 'category', 
        'date_created', 'application', 'hardware', 'author'
    ]
    search_fields = ['title']

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

    readonly_fields = ['cached_image_path']

    def get_urls(self):
        urls = super(PhotoAdmin, self).get_urls()
        my_urls = patterns("",
            url(r"^import_photos/$", import_photos)
        )
        return my_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['categories'] = Photo.CATEGORIES
        return super(PhotoAdmin, self).changelist_view(request,
            extra_context = extra_context
        )

    def save_model(self, request, object, form, change):
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

        # pyexiv2 doesn't work with the gif format
        if imghdr.what(object.cached_image_path) != "gif":
            object.generate_image_xmp_metadata()
        
admin.site.register(Photo, PhotoAdmin)

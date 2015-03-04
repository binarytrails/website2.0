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

from django.contrib import admin
from frontend.models import Photo

class PhotoAdmin(admin.ModelAdmin):
	# Select Form
	list_display = ['title', 'category']
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

		if make_thumbnails:
			object.generate_thumbnails()

		object.generate_image_xmp_metadata()
		
admin.site.register(Photo, PhotoAdmin)

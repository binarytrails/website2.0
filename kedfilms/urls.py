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

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',

    # frontend

    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'frontend.views.home', name='home'),

    url(r'^projects/$', 'frontend.views.projects', name='projects'),

    url(r'^articles/$', 'frontend.views.articles', name='articles'),
    url(r'^article/(?P<article_id>[\d]{1,4})/$', 'frontend.views.article', name='article'),

    url(r'^photos/$', 'frontend.views.photos', name='photos'),
    url(r'^photos/gallery/(?P<category_id>[\d]{1,4})/$', 'frontend.views.gallery',
        name='gallery'),
    url(r'^photos/slideshow/(?P<category_id>[\d]{1,4})/(?P<fragment_id>[\w\-._]{1,41})/$',
        'frontend.views.slideshow', name='slideshow'),

    url(r'^videos/$', 'frontend.views.videos', name='videos'),
    
    # cart

    url(r'^cart/(?P<folder>[\w\-_]{1,15})/(?P<html_file>[\w\-_]{1,15})/$',
        'cart.views.project', name='cart'),

    # only for localhost not in production
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'frontend.views.error404'

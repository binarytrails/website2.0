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

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'frontend.views.home', name='home'),

    url(r'^articles/$', 'frontend.views.articles', name='articles'),
    url(r'^artcile/(?P<category>[\w\-]{1,10})/(?P<article>[\w\-]{1,30})$', 'frontend.views.article', name='article'),

    url(r'^photos/$', 'frontend.views.photos', name='photos'),
    url(r'^photos/gallery/(?P<category>[\w\_]{1,20})/$', 'frontend.views.gallery', name='gallery'),
    url(r'^photos/slideshow/(?P<category>[\w]{1,20})/(?P<fragment_id>[\w\-._]{1,41})/$', 'frontend.views.slideshow', name='slideshow'),

    url(r'^videos/$', 'frontend.views.videos', name='videos'),
    
    # only for localhost not in production
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'frontend.views.error404'

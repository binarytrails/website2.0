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

from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from frontend import views as frontend
from cart import views as cart

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # frontend
    url(r'^$', frontend.home, name='home'),

    url(r'^projects/$', frontend.projects, name='projects'),

    url(r'^articles/$', frontend.articles, name='articles'),
    url(r'^article/(?P<article_id>[\d]{1,4})/$', frontend.article, name='article'),

    url(r'^photos/$', frontend.photos, name='photos'),
    url(r'^photos/gallery/(?P<category_id>[\d]{1,4})/$', frontend.gallery,
        name='gallery'),
    url(r'^photos/slideshow/(?P<category_id>[\d]{1,4})/(?P<fragment_id>[\w\-._]{1,41})/$', frontend.slideshow, name='slideshow'),

    url(r'^videos/$', frontend.videos, name='videos'),

    # cart
    url(r'^cart/(?P<folder>[\w\-_]{1,15})/(?P<html_file>[\w\-_]{1,15})/$',
        cart.project, name='cart'),
]
# only for localhost not in production
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = frontend.error404


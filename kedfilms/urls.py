from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    
    # sections
    url(r'^$', 'frontend.views.home', name='home'),

    url(r'^articles/', 'frontend.views.articles', name='articles'),
    url(r'^artciles/(?P<section>[\w]{1,10})/(?P<article>[\w\-]{1,20})$', 'frontend.views.articles', name='articles'),

    url(r'^photos/$', 'frontend.views.photos', name='photos'),
    url(r'^photos/slideshow/(?P<category>[\w]{1,10})/$', 'frontend.views.photos_slideshow', name='photos_slideshow'),

    url(r'^videos/', 'frontend.views.videos', name='videos'),

    # admin
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)

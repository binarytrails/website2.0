from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'frontend.views.home', name='home'),

    url(r'^articles/$', 'frontend.views.articles', name='articles'),
    url(r'^artcile/(?P<section>[\w\-]{1,10})/(?P<article>[\w\-]{1,20})$', 'frontend.views.article', name='article'),

    url(r'^photos/gallery/(?P<section>[\w]{1,10})/$', 'frontend.views.gallery', name='gallery'),
    url(r'^photos/slideshow/(?P<category>[\w]{1,10})/$', 'frontend.views.slideshow', name='slideshow'),

    url(r'^videos/$', 'frontend.views.videos', name='videos'),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    
    url(r'^$', 'frontend.views.home', name='home'),

    url(r'^articles/$', 'frontend.views.articles', name='articles'),
    url(r'^artcile/(?P<section>[\w\-]{1,10})/(?P<article>[\w\-]{1,20})$', 'frontend.views.article', name='article'),

    url(r'^photos/gallery/(?P<section>[\w]{1,10})/$', 'frontend.views.gallery', name='gallery'),
    url(r'^photos/slideshow/(?P<category>[\w]{1,10})/$', 'frontend.views.slideshow', name='slideshow'),

    url(r'^videos/$', 'frontend.views.videos', name='videos'),

)

handler404 = 'frontend.views.error404'

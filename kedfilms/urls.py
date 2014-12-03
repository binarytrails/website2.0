from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    
    url(r'^$', 'frontend.views.entry', name='entry'),

    url(r'^home/$', 'frontend.views.home', name='home'),

    url(r'^articles/$', 'frontend.views.articles', name='articles'),
    url(r'^artcile/(?P<category>[\w\-]{1,10})/(?P<article>[\w\-]{1,30})$', 'frontend.views.article', name='article'),

    url(r'^photos/$', 'frontend.views.photos', name='photos'),
    url(r'^photos/gallery/(?P<category>[\w]{1,10})/$', 'frontend.views.gallery', name='gallery'),
    url(r'^photos/slideshow/(?P<category>[\w]{1,10})/$', 'frontend.views.slideshow', name='slideshow'),
    url(r'^photos/mslideshow/(?P<category>[\w]{1,10})/(?P<image>[\w\-._]{1,30})/$', 'frontend.views.mslideshow', name='mslideshow'),

    url(r'^videos/$', 'frontend.views.videos', name='videos'),
)

handler404 = 'frontend.views.error404'

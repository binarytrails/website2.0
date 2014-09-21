from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^photos/', 'frontend.views.photos', name='photos'),
    url(r'^articles/', 'frontend.views.articles', name='articles'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from alternativ import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alternativ.views.home', name='home'),
    # url(r'^alternativ/', include('alternativ.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # other urls
    url(r'^$', views.index, name='index'),
    # handle invalid url requests in the views functions below...
    url(r'^(?P<item>\w+)/$', views.detail, name='detail'),
    url(r'^(?P<item_type>\w+)/(?P<item>\w+)/$', views.options, name='options'),
    # static about-page
    url(r'^about$', views.about, name='about')
)

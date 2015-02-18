from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin-dashboard/', include(admin.site.urls)),

    url(r'^', include('cms.urls')),
    #url(r'^', include('core.urls')),
)


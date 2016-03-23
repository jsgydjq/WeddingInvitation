from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin$', include(admin.site.urls)),
    (r'^$',  'fslss.views.home'),
    (r'^web$',  'fslss.views.index'),
    (r'^web/impress/$',  'fslss.views.impress'),

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

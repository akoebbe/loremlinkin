from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'links.views.index', name='home'),
    url(r'^(?P<link_hash>[A-Fa-f0-9]{10})$', 'links.views.view', name='view'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

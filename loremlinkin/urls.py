from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers
from links import views

router = routers.SimpleRouter()
router.register(r'links', views.LinkViewSet, base_name='link')

urlpatterns = patterns('',
    url(r'^$', 'links.views.index', name='home'),
    url(r'^(?P<link_hash>[A-Za-z0-9]+)$', 'links.views.view', name='link-detail'),
    url(r'^(?P<link_hash>[A-Za-z0-9]+)/clone$', 'links.views.index', name='link-clone'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls, namespace="api")),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
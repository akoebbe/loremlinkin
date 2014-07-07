from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from links import views

router = routers.DefaultRouter()
router.register(r'links', views.LinkViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'links.views.index', name='home'),
    url(r'^(?P<link_hash>[A-Fa-f0-9]{10})$', 'links.views.view', name='view'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
)

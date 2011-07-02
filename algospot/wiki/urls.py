# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
import views

urlpatterns = patterns('wiki.views',
        url(r'^read/(?P<slug>.+)$', views.detail, name='wiki-detail'),
        url(r'^edit/(?P<slug>.+)$', views.edit, name='wiki-edit'),
        url(r'^history/(?P<slug>.+)$', views.history, name='wiki-history'),
        url(r'^old/(?P<id>[0-9]+)/(?P<slug>.+)$', views.old, 
            name='wiki-old'),
        url(r'^revert/(?P<id>[0-9]+)/(?P<slug>.+)$', views.revert, 
            name='wiki-revert'),
        )


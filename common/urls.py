# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('common.views',
    url(r'^contacto/$', "contacto", name="contacto"),
)

# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('marcas.views',
    url(r'^$', "marcas", name="marcas"),
    url(r'^showroom/(?P<id_marca>\d+)/(?P<id_categoria>\d+)/$', "categorias", 
        name="categorias"),
    url(r'^showroom/modelos/(?P<id_modelo>\d+)/$', "modelos", 
        name="modelos"),
)

# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('empresas.views',
    url(r'^nosotros/$', "info_empresa",
        {"template": "empresas/nosotros.html", 
         "titulo": u"Nosotros"},
        name="nosotros"),
    url(r'^mision_vision/$', "info_empresa",
        {"template": "empresas/mision.html", 
         "titulo": u"Misión y visión"},
        name="mision"),
    url(r'^politicas_calidad/$', "info_empresa",
        {"template": "empresas/politicas.html", 
         "titulo": u"Políticas de calidad"},
        name="politicas"),
    url(r'^servicios/$', "servicios", name="servicios"),
    url(r'^filiales/$', "filiales", name="filiales"),
)

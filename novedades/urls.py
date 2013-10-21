# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from novedades.models import Evento, Promocion, Noticia, Enlace, Evento_home


urlpatterns = patterns('novedades.views',
    url(r'^eventos/$', "novedades", 
        {"model": Evento,
         "template": "novedades/novedades.html",
         "titulo": u"Home/Eventos"}, 
        name="eventos"),
    url(r'^promociones/$', "novedades", 
        {"model": Promocion,
         "template": "novedades/novedades.html",
         "titulo": u"Promociones"}, 
         name="promociones"),
    url(r'^noticias/$', "novedades", 
        {"model": Noticia,
         "template": "novedades/novedades.html",
         "titulo": u"Noticias"}, 
         name="noticias"),
    url(r'^enlaces/$', "novedades", 
        {"model": Enlace,
         "template": "novedades/enlaces.html",
         "titulo": u"Enlaces"}, 
         name="enlaces"),
    url(r'^home/$', "novedades", 
        {"model": Evento_home,
         "template": "novedades/eventos_home.html",
         "titulo": u"Home"}, 
         name="eventos_home"),
)

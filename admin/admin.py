# -*- coding: utf-8 -*-

from django.contrib import admin
# models
from empresas.models import *
from marcas.models import *
from novedades.models import *

# empresas
admin.site.register(Empresa)
admin.site.register(Servicio)
admin.site.register(Filial)
# marcas
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Modelo)
# novedades
admin.site.register(Evento)
admin.site.register(Evento_home)
admin.site.register(Promocion)
admin.site.register(Noticia)
admin.site.register(Enlace)

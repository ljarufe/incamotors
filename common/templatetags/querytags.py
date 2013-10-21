# -*- coding: utf-8 -*-

from django.core.cache import cache
from django import template
from django.db.models import Min
# models
from marcas.models import Marca, Categoria


register = template.Library()

@register.inclusion_tag('common/templatetags/cache_marcas.html')
def get_marcas():
    """
    Retorna la lista de marcas
    """
    marcas = cache.get('cache_marcas')
    if not marcas:
        marcas = Marca.objects.all()
        cache.set('cache_marcas', marcas)
    return {'marcas': marcas}


@register.inclusion_tag('common/templatetags/cache_showroom.html')
def get_showroom_home():
    """
    Retorna el primer auto de la primera marca al hacer click sobre
    showroom en el menu
    """
    ids = cache.get('cache_showroom')
    if not ids:
        marca = Marca.objects.all().aggregate(Min('id'))
        categoria = Categoria.objects.all().aggregate(Min('id'))
        ids = {'marca': marca['id__min'],
               'categoria': categoria['id__min']}
        cache.set('cache_showroom', ids)
        
    return {'ids': ids}


# -*- coding: utf-8 -*-

from common.utils import direct_response
from django.shortcuts import get_list_or_404
# models
from novedades.models import Evento


def novedades(request, model, template, titulo):
    """
    Vista genérica para los 3 tipos de novedades y enlaces
    """

    novedades = get_list_or_404(model)
    return direct_response(request, template,
                           {"novedades": novedades,
                            "titulo": titulo})

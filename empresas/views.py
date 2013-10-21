# -*- coding: utf-8 -*-

from common.utils import direct_response
from django.shortcuts import get_object_or_404
# models
from empresas.models import Empresa, Servicio, Filial


def info_empresa(request, template, titulo):
    """
    Vista de la información de la empresa
    """
    empresa = get_object_or_404(Empresa, id=1)
    
    return direct_response(request, template,
                           {'empresa': empresa,
                            'titulo': u"%s" % titulo})


def servicios(request):
    """
    Lista de servicios de la empresa
    """
    servicios = Servicio.objects.all()
    
    return direct_response(request, "empresas/servicios.html",
                           {"servicios": servicios,
                            "titulo": "Servicios"})
                            

def filiales(request):
    """
    Lista de servicios de la empresa
    """
    filiales = Filial.objects.all()
    
    return direct_response(request, "empresas/filiales.html",
                           {"filiales": filiales,
                            "titulo": "Filiales"})


# -*- coding: utf-8 -*-

from common.utils import direct_response
from django.shortcuts import get_object_or_404, get_list_or_404
# models
from marcas.models import Marca, Categoria, Modelo


def marcas(request):
    """
    Lista de marcas y su descripción
    """
    marcas = Marca.objects.all()
    
    return direct_response(request, "marcas/marcas.html",
                           {"marcas": marcas,
                            "titulo": "Marcas"})
                            
                            
def categorias(request, id_marca, id_categoria):
    """
    Lista de modelos de una categoría por marca
    """
    marca = get_object_or_404(Marca, id=id_marca)
    categorias = Categoria.objects.filter(marca=marca)
    modelos = get_list_or_404(Modelo, categoria__id=id_categoria)
    
    return direct_response(request, "marcas/categorias.html",
                           {"marca": marca,
                            "categorias": categorias,
                            "modelos": modelos,
                            "id_categoria": id_categoria,
                            "titulo": "Showroom: %s" % marca.nombre})
                            
                            
def modelos(request, id_modelo):
    """
    Datos y fotos de un modelo en el showroom
    """
    modelo = get_object_or_404(Modelo, id=id_modelo)
    categorias = Categoria.objects.filter(marca=modelo.categoria.marca)
    modelos = Modelo.objects.filter(categoria=modelo.categoria)
    
    return direct_response(request, "marcas/modelos.html",
                           {"modelo": modelo,
                            "categorias": categorias,
                            "modelos": modelos,
                            "marca": modelo.categoria.marca,
                            "categoria": modelo.categoria.id,
                            "next": modelo.id+1,
                            "titulo": "Showroom: %s de %s" % \
                                      (modelo, modelo.categoria.marca)})    
    

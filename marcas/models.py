# -*- coding: utf-8 -*-

from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField


class Marca(models.Model):
    """
    Marca de autos
    """
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    logo = ImageWithThumbnailsField(
                upload_to='img/marcas',
                thumbnail={'size': (200, 200),"extension":"png"},
                extra_thumbnails={'small': {'size': (100, 100),"extension":"png"}},
                generate_on_save=True,
            )
            
    def __unicode__(self):
        return '%s' % self.nombre
            

class Categoria(models.Model):
    """
    Categoria dentro de una marca
    """
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca)
    
    def __unicode__(self):
        return '%s - %s' % (self.nombre, self.marca)
    
    
class Modelo(models.Model):
    """
    Modelo de auto dentro de una categoría
    """
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria)
    foto_lat = ImageWithThumbnailsField(
            upload_to='img/modelos',
            thumbnail={'size': (300, 300)},
            extra_thumbnails={'small': {'size': (100, 100)}},
            generate_on_save=True,
        )
    foto_int = ImageWithThumbnailsField(
                upload_to='img/modelos',
                thumbnail={'size': (300, 300)},
                extra_thumbnails={'small': {'size': (100, 100)}},
                generate_on_save=True,
                null=True,
                blank=True,
            )
    foto_back = ImageWithThumbnailsField(
                upload_to='img/modelos',
                thumbnail={'size': (300, 300)},
                extra_thumbnails={'small': {'size': (100, 100)}},
                generate_on_save=True,
                null=True,
                blank=True,
            )
    ficha = models.FileField(upload_to="files/fichas", blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.nombre


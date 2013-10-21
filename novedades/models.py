# -*- coding: utf-8 -*-

from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField


class Novedad(models.Model):
    """
    Clase abstracta para todas las novedades
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name=u"descripción")
    
    def __unicode__(self):
        return '%s' % self.nombre
        
    class Meta:
        abstract = True


class Evento(Novedad):
    """
    Eventos de la página de inicio
    """
    foto = ImageWithThumbnailsField(
                upload_to = 'img/eventos',
                thumbnail = {'size': (625, 420),
                           'options': ['upscale', 'max', 'crop']},
                generate_on_save = True,
            )


class Evento_home(Novedad):
    """
    Eventos para la página de inicio
    """
    foto = ImageWithThumbnailsField(
                upload_to = 'img/eventos',
                thumbnail = {'size': (625, 420),
                           'options': ['upscale', 'max', 'crop']},
                generate_on_save = True,
            )
    foto_pie = ImageWithThumbnailsField(
                    upload_to = 'img/eventos',
                    thumbnail = {'size': (625, 220),
                               'options': ['upscale', 'max', 'crop']},
                    generate_on_save = True,
                )
                
    class Meta:
        verbose_name = u"Evento en home"
        verbose_name_plural = u"Eventos en home"

    
class Promocion(Novedad):
    """
    Promociones de incamotors, iguales a los eventos
    """
    foto = ImageWithThumbnailsField(
                upload_to = 'img/promociones',
                thumbnail = {'size': (625, 420),
                           'options': ['upscale', 'max', 'crop']},
                generate_on_save = True,
            )
            
    class Meta:
        verbose_name = u"promoción"
        verbose_name_plural = u"promociones"
        

class Noticia(Novedad):
    """
    Noticias del menu superior
    """
    foto = ImageWithThumbnailsField(
                upload_to = 'img/noticias',
                thumbnail = {'size': (625, 420),
                           'options': ['upscale', 'max', 'crop']},
                generate_on_save = True,
            )


class Enlace(models.Model):
    """
    Enlaces a otros sitios web
    """
    url = models.URLField()
    descripcion = models.TextField(verbose_name=u"descripción")
    
    def __unicode__(self):
        return u"%s" % self.url


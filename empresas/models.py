# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Max


class Empresa(models.Model):
    """
    Datos dinamicos para Incamotors
    """
    nombre = models.CharField(max_length=50)
    nosotros = models.TextField()
    mision = models.TextField(verbose_name=u"Misión")
    vision = models.TextField(verbose_name=u"Visión")
    politicas = models.TextField(verbose_name=u"Políticas de calidad")

    def __unicode__(self):
        return '%s' % self.nombre

    def save(self, *args, **kwargs):
        """
        Si se crea una nueva empresa la anterior desaparecerá
        """
        old_id = Empresa.objects.aggregate(Max('id'))
        try:
            empresa = Empresa.objects.get(id=old_id['id__max'])
            empresa.delete()
        except Empresa.DoesNotExist:
            pass
        return super(Empresa, self).save(*args, **kwargs)
        

class Servicio(models.Model):
    """
    Servicio prestado por la empresa
    """
    nombre = models.TextField()
    
    def __unicode__(self):
        return '%s' % self.nombre
    
    
class Filial(models.Model):
    """
    Filial de la empresa
    """
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return '%s' % self.nombre
        
    class Meta:
        verbose_name_plural = u"Filiales"


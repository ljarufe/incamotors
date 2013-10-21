# -*- coding: utf-8 -*-

from django import forms
from common.validators import validate_name, validate_phone


class ContactoForm(forms.Form):
    """
    Formulario de contacto
    """
    DIR_CHOICES = (
        (u'X', u'Nombre X]'),
    )
    dirigido_a = forms.ChoiceField(choices=DIR_CHOICES)
    nombre = forms.CharField(validators=[validate_name])
    DEP_CHOICES = (
        (u'X', u'Departamento X]'),
    )
    departamento = forms.ChoiceField(choices=DEP_CHOICES)
    direccion = forms.CharField()
    telefono = forms.CharField(validators=[validate_phone])
    email = forms.EmailField(label=u"e-mail")
    mensaje = forms.CharField(widget=forms.Textarea)

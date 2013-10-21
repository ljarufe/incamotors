# -*- coding: utf-8 -*-

from common.utils import direct_response
from novedades.models import Evento
from common.forms import ContactoForm
from common.utils import send_html_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def inicio(request):
    """
    Vista de inicio
    """
    return direct_response(request, "common/inicio.html",
                           {"titulo": "Inicio"})
    

@csrf_exempt    
def contacto(request):
    """
    Formulario de contacto con la empresa
    """
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            #Envío del e-mail
            subject = 'Contacto via web con ' + form.cleaned_data['nombre']
            data = (form.cleaned_data['dirigido_a'],
                    form.cleaned_data['departamento'],
                    form.cleaned_data['nombre'],
                    form.cleaned_data['direccion'],
                    form.cleaned_data['telefono'],
                    form.cleaned_data['email'],
                    form.cleaned_data['mensaje'])                    
            # TODO: el mail de envío y recepción deben ser cambiados
            send_html_mail(subject, 'contacto.html', data, 
                           'luis.jarufe@hotmail.com', ['luis.jarufe@hotmail.com'])
            return HttpResponseRedirect(reverse('inicio'))
    else:
        form = ContactoForm()
        
    return direct_response(request, 'common/contacto.html',
                           {'form': form,
                           'titulo': 'Contacto'})
                              

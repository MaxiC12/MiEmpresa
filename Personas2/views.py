
from django.shortcuts import render, redirect
from .models import Persona
from .form import FormPersona, ContactoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import View
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import Context
from django.http import HttpResponse, FileResponse

from django.core.mail import EmailMessage
from time import timezone


def index(request):
    return render(request,'Persona2/index.html')


def Listado(request):
   personas=Persona.objects.all()
   return render(request,'Persona2/Listado.html', {'personas': personas})

def contacto(request):
    form_contacto= ContactoForm()
    if request.method == 'POST':
        form_contacto = ContactoForm(request.POST)
    if form_contacto.is_valid():    
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
    # Envía el correo electrónico
        send_mail(
            'Contacto',
            f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
            'tu_email@dominio.com', 
            # Dirección de correo electrónico del remitente
            ['correo_destino@dominio.com'], # Lista de destinatarios
            fail_silently=False,
            )    
        return redirect('contacto_recibido')
    else:
    messages.error('Error. Por favor verifica que los datos este correctos.')
    # Lógica adicional, como enviar una respuesta o redirigir a una página de agradecimiento
    return render(request, 'Persona2/contacto.html', {'form_contacto':form_contacto})

        
def nueva(request):
    if request.method == 'POST':
        formpersona= FormPersona(request.POST, request.FILES)
        if formpersona.is_valid():  
            formpersona.save()
            return redirect('Listado')
    else:
        formpersona=FormPersona()
    return render(request, 'persona2/nueva.html', {'formpersona':FormPersona})

def editar(request, id):
    persona= get_object_or_404(Persona,pk=id)
    if request.method == 'POST': 
        formpersona= FormPersona(request.POST, request.FILES, instance=persona)
        if formpersona.is_valid():
            formpersona.save()
            return redirect('Listado')
    else:
        formpersona=FormPersona(instance=persona)
    return render(request, 'persona2/editar.html',{'formpersona':formpersona})

def eliminar(request, id ):
    borrar_persona= get_object_or_404(Persona,pk=id)
    if request.method=='POST':
        formpersona= FormPersona(request.POST, instance=borrar_persona)
        borrar_persona.delete()
        return redirect('Listado')
    return render(request, 'persona2/eliminar.html',{'formpersona':borrar_persona})


@login_required
def change_password(request): 
    return PasswordChangeView.as_view(
    templates_name='registration/change_password.html',
    sucess_url=reverse_lazy('index'))
    


import os
from django.http import HttpResponse, FileResponse
from django.template.loader import get_template
import requests
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class generar_lista(View):
    def link_callback(self,uri,rel):
        sUrl = settings.STATIC_URL
        sRoot = settings.STATIC_ROOT
        mUrl = settings.MEDIA_URL
        mRoot = settings.MEDIA_ROOT

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri
        
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' %(sUrl, mUrl)
            )
        return path

    def get(self, request, *args,**kwrags):
        template = get_template('reporte_personas.html')
        context= {
            'reporte': Persona.objects.all(),
            'logo': '{}{}'.format(settings.MEDIA_URL, 'logoISSM.jpg')
            }
        html = template.render(context)
        response = HttpResponse(content_type='Persona/pdf')
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"' #para que el archivo se descargue automaticante
        pisaStatus = pisa.CreatePDF(
            html, dest=response,
            link_callback=self.link_callback
            )
        if pisaStatus.err:
            return HttpResponse ('Ocurrió un error <pre>' + html + '</pre>')   
        return response 



def Listaclientes(request):
    personas = Persona.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(personas, 3)  #  paginate_by 5
    try:
        personas = paginator.page(page)
    except PageNotAnInteger:
        personas = paginator.page(1)
    except EmptyPage:
        personas = paginator.page(paginator.num_pages)
    return render(request, "Persona2/Lista_persona.html", {"personas": personas})
# Create your views here.

#import email
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from Academia.models import Estudiante

# Create your views here.
def formularioContacto(request):
    return render(request, 'formularioContacto.html')

def contactar(request):
    if request.method == 'POST':
        asunto = request.POST['txtAsunto']
        mensaje = request.POST['txtMensaje'] + '/ Email: ' + request.POST['txtEmail']
        email_desde = settings.EMAIL_HOST_USER
        email_para = ['mas.levario.online@gmail.com']
        send_mail(asunto,mensaje,email_desde,email_para,fail_silently=False)
        return render(request,'contactoExitoso.html')
    return render(request, 'formularioContacto.html')

def academia(request):
    return render(request, 'contacto.html')

def busqueda_Estudiante(request):
    return render(request, 'busquedaEstudiantes.html')

def buscar(request):
    if request.GET['est']:
        #mensaje = "Estudiante buscado: %r" %request.GET['est']
        est = request.GET['est']
        if len(est) > 50:
            mensaje = 'Nombres demaciado largo.'
        else:
            estudiantes = Estudiante.objects.filter(nombres__icontains=est)
            return render(request, 'resultados_busqueda.html', {'estudiantes': estudiantes, 'query': est})
    else:
        mensaje = 'No has entroducido algo'
    return HttpResponse(mensaje)
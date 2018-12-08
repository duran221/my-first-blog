from django.shortcuts import render


from django.utils import timezone

#Importando el modelo publicacion (objeto)
from .models import Publicacion

# Create your views here.

#Creando una view llamada lista_publicaciones
def lista_publicaciones(request):

    #Realizando la consulta en la base de datos: QuerySet
    publicaciones= Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')

    #request: (todo lo que recibimos del usuario via Internet)
    #'miblog/lista_publicaciones.html': Ruta de la plantilla
    #{} :es un lugar en el que podemos agregar algunas cosas para que la plantilla las use
    return render(request,'miblog/lista_publicaciones.html',{'publicaciones':publicaciones})




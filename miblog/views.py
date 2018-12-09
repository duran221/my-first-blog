from django.shortcuts import render,get_object_or_404


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



"""
    permite retornar una vista hacia la direccion 'miblog/detalles_publicacion.html'
    request:
    pk: Llave primaria o numero consecutivo de la base de datos
"""
def detalles_publicacion(request,pk):

        publicacion= get_object_or_404(Publicacion,pk=pk)
        return render(request,'miblog/detalles_publicacion.html',{'publicacion':publicacion})







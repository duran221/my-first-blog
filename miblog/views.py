from distutils import command

from django.shortcuts import render,get_object_or_404


from django.utils import timezone

#Importando el modelo Publicacion (objeto)
from .models import Publicacion

#importando la clase Formulario_Publicacion
from .forms import Formulario_Publicacion

from django.shortcuts import redirect

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

def nueva_publicacion(request):
    #validando si el metodo de envio de datos es POST
    if(request.method=='POST'):
        #Instanciando nuestro formulario
        formulario = Formulario_Publicacion(request.POST)

        #si todos los campos necesarios están definidos y no hay valores incorrectos
        if formulario.is_valid():
            #Guardamos el formulario
            publicacion = formulario.save(commit=False)
            #obteniendo el autor (el usuario)
            publicacion.autor = request.user
            #estableciendo la fecha de publicacion
            publicacion.fecha_publicacion = timezone.now()
            #guardando el formulario
            publicacion.save()
            #redirigiendo la pagina hacia el enlace de publicacion
            return redirect('detalles_publicacion', pk=publicacion.pk)


    else:
        #instanciando el objeto Formulario: IMPORTANTE DECLARAR COMO 'FORM'
        form= Formulario_Publicacion
        #IMPORTANTE INDICAR EN EL TERCER PARAMETRO COMO FORM, YA QUE ESTOS DATOS SON RECOGIDOS POR LA PLANTILLA
        return render(request,'miblog/editar_publicacion.html',{'form':form})


def editar_publicacion(request,pk):
    #1 Obteniendo una instancia de la publicacion a editar:
    publicacion= get_object_or_404(Publicacion,pk=pk)
    #Preguntando si el metodo de envio de datos es POST
    if(request.method=='POST'):
        #creando una nueva instancia del formulario a editar
        formulario= Formulario_Publicacion(request.POST,instance=publicacion)
        #Preguntando si el formulario no contiene errores y sus campos son completos
        if(formulario.is_valid()):

            #Guardando el formulario sin antes
            publicacion= formulario.save(commit=False)
            publicacion.autor=request.user
            publicacion.fecha_publicacion= timezone.now()
            publicacion.save()
            return redirect('detalles_publicacion',pk=publicacion.pk)

    else:
        #Instanciando el objeto tipo formulario, pasamos como instancia la publicacion a editar
        form= Formulario_Publicacion(instance=publicacion)
        return render(request,'miblog/editar_publicacion.html',{'form':form})




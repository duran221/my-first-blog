from django.shortcuts import render

# Create your views here.

def lista_publicaciones(request):
    return render(request,'miblog/lista_publicaciones.html',{})

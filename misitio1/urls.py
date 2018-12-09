"""misitio1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    #dice que para cada URL que empieza con admin/ Django encontrará su correspondiente view.
    #  En este caso estamos incluyendo muchas URLs admin así que no todo está empaquetado en este pequeño archivo.
    #  Es más limpio y legible.
    path('admin/', admin.site.urls),

    #Importar o incluir el archivo urls incluido en el directorio "miblog"
    #Ahora Django redirigirá todo lo que entre a 'http://127.0.0.1:8000/' hacia blog.urls y buscará más instrucciones allí.
    
    path('',include('miblog.urls'))
]




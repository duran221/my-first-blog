
#Aquí estamos importando la función de Django path

from django.urls import path


#todos nuestras views desde la aplicación blog

from . import views

#Segundo parametro: Asociando una vista (view) llamada post_list a la URL raíz
#Tercer Parametro:  name='post_list' es el nombre de la URL que se utilizará para identificar a la vista.
urlpatterns = [path('', views.lista_publicaciones,name= 'lista_publicaciones')]

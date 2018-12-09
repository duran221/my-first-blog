
#Aquí estamos importando la función de Django path

from django.urls import path


#todos nuestras views desde la aplicación blog

from . import views

#Segundo parametro: Asociando una vista (view) llamada post_list a la URL raíz
#Tercer Parametro:  name='post_list' es el nombre de la URL que se utilizará para identificar a la vista.
urlpatterns = [path('', views.lista_publicaciones,name= 'lista_publicaciones'),
               path('publicacion/<int:pk>/',views.detalles_publicacion,name='detalles_publicacion')]
            #En la anterior linea: 1.Parametro: 'publicacion/' la url deberia empezar con dicha palabra seguido de '/'
            #int:pk/->Significa que Django buscará un número entero y se lo pasará a la vista en una variable llamada pk.
            #Esto quiere decir que si pones http://127.0.0.1:8000/post/5/ en tu navegador, Django entenderá que estás buscando
            #una vista llamada post_detail y transferirá la información de que pk es igual a 5 a esa vista.

    
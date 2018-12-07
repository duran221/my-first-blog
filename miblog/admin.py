from django.contrib import admin

#Importando la clase (objeto Publicacion):

from .models import Publicacion

# Register your models here.


# Para hacer nuestro modelo visible en la página del administrador, tenemos que registrar el modelo con
admin.site.register(Publicacion)


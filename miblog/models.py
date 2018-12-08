from django.db import models

#importando la zona horaria de django

from django.utils import timezone

# Create your models here.


#esta línea define nuestro modelo (es un objeto). CLASE
#models.Model significa que Publicacion es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
class Publicacion(models.Model):

    #models.CharField, así es como defines un texto con un número limitado de caracteres.
    titulo= models.CharField(max_length=200)

    #este es una relación (link) con otro modelo. (Llave foranea)
    autor= models.ForeignKey("auth.User", on_delete=models.CASCADE)

    #este es para texto largo sin límite. Suena perfecto para el contenido de la entrada del blog, ¿no?
    texto = models.TextField()

    #este es fecha y hora.
    fecha_creacion= models.DateField(default=timezone.now())

    #null-True: se permiten valores nulos en la tabla de Database
    fecha_publicacion= models.DateField(blank=True,null=True)


    """
    Metodo permite realizar una publicacion
    
    """
    def publicar(self):
        #Asignando la fecha actual del ordenador:
        self.fecha_publicacion= timezone.now()

        #Guarda en la base de datos nuestros datos.
        self.save()


    """
    Retornar el titulo de la publicacion
    """
    def __str__(self):

        return self.titulo






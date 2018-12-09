from django import forms

#Importando el modelo Publicacion
from .models import Publicacion

#Nuestro formulario (Una clase de tipo ModelForm)
class Formulario_Publicacion(forms.ModelForm):


    class Meta:
        #Importante declarar los campos con sus respectivos nombres: model y fields
        model = Publicacion
        #campos a incluir en nuestro formulario para ser ingresados
        fields = ('titulo','texto',)
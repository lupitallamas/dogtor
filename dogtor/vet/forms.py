from django import forms
from.models import PetOwner, Pet

#Los formularios se tienen que vincular con los modelos

#los formularios -->classmethod

class OwnerForm(forms.ModelForm):
    #1, Modelo de nuesto formulario
    #2. fields que van a est en nuestro formulario

    class Meta:
        model = PetOwner #1
        fields=("first_name","last_name","address","email","phone")
        
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields=("name","type","owner")   
        
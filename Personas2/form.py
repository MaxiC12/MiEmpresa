from django import forms , EmailInput
from .models import Persona, Contacto




class FormPersona(forms.ModelForm):
    class Meta:
        model=Persona
        fields='__all__'


class ContactoForm(forms.ModelForm):
    class Meta:
      model = Contacto
      fields = '__all__'
      widgets = {'email': EmailInput(attrs={'type': 'email'})}



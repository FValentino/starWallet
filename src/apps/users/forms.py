from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class FormUser(UserCreationForm):

    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(label="Apelido", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))
    cuil = forms.CharField(label="Cuil", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su numero de CUIL',  'maxlength':'11' }))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su correo electronico'}))
    tel = forms.CharField(label="Telefono", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su telefono'}))
    birthdate = forms.CharField(label="fecha de nacimiento", widget=forms.DateInput(attrs={'placeholder': 'AAAA-MM-DD', 'type': 'date'}))
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'placeholder': 'Ingrese un nombre de usuario'}))
    perfil_pic = forms.ImageField(label="Foto de perfil", required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'cuil', 'email', 'tel', 'birthdate', 'username', 'password1', 'password2', 'perfil_pic']
    
    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)

        add_class_form_control = ['first_name', 'last_name', 'cuil', 'email', 'tel', 'birthdate', 'username', 'password1', 'password2', 'perfil_pic']
        
        for attr_field in add_class_form_control:
            self.fields[attr_field].widget.attrs["class"] = "form-control"
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.cuil = self.cleaned_data['cuil']
        user.tel = self.cleaned_data['tel']
        user.birthdate = self.cleaned_data['birthdate']
        user.perfil_pic = self.cleaned_data.get('perfil_pic')
        if commit:
            user.save()
        return user

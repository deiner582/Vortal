#encoding: utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from Admin.models import *



class FormularioCorreo(forms.Form):
    Celular=forms.CharField(label='Celular',required=True)
    Nombre = forms.CharField(label='Nombre:', max_length=100,required=True)
    Asunto= forms.CharField(label='Asunto:',required=True)
    Correo=forms.EmailField(required=True)
    Mensaje= forms.CharField(label='Mensaje:',widget=forms.Textarea,required=True)

class FormularioLogin(forms.Form):
    usuario=forms.CharField(label='Usuario :  ',required=True)
    contrasena=forms.CharField(label='Contrasena :  ',required=True,widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(

        PrependedText('usuario', '<span class="glyphicon glyphicon-user"></span>', active=True),
        PrependedText('contraseña', '<span class="glyphicon glyphicon-asterisk"></span>'),
        'multicolon_select',


    )






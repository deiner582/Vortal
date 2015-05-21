# -*- coding: latin-1 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Estudiante



class FormularioLogin(forms.Form):
    usuario=forms.CharField(label='Usuario :  ',required=True)
    contrasena=forms.CharField(label='Contrasena :  ',required=True,widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(

        PrependedText('usuario', '<span class="glyphicon glyphicon-user"></span>', active=True),
        PrependedText('contrasena', '<span class="fa fa-key"></span>'),
        'multicolon_select',


    )
class FormularioRegistro(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields = ['tipo_documento','documento','lugar_expedicion','fecha_expedicion','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','sexo','lugar_nacimiento','fecha_nacimiento','direccion','telefono','correo','programa','estrato','etnia']
        widgets={
            'tipo_documento':forms.Select(attrs={'class':'form-control','required': True}),
            'documento':forms.TextInput(attrs={'class':'form-control','placeholder':'digite documento','required': True}),
            'lugar_expedicion':forms.Select(attrs={'class':'form-control','required': True}),
            'fecha_expedicion':forms.TextInput(attrs={'class':'form-control','data-date-format':'DD/MM/YYYY'}),
            'primer_nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'digite documento','required': True}),
            'segundo_nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'digite documento'}),
            'primer_apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'digite documento','required': True}),
            'segundo_apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'digite documento','required': True}),
            'sexo':forms.Select(attrs={'class':'form-control','required': True}),
            'lugar_nacimiento':forms.Select(attrs={'class':'form-control','required': True}),
            'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control','data-date-format':'DD/MM/YYYY'}),
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'digite documento','required': True}),
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'digite documento','required': True}),
            'correo':forms.TextInput(attrs={'class':'form-control','placeholder':'digite documento','required': True}),
            'programa':forms.Select(attrs={'class':'form-control','required': True}),
            'estrato':forms.Select(attrs={'class':'form-control','required': True}),
            'etnia':forms.Select(attrs={'class':'form-control','required': True}),
            'estado':forms.Select(attrs={'class':'form-control','required': True}),

        }





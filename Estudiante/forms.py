# -*- coding: latin-1 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions



class FormularioLogin(forms.Form):
    usuario=forms.CharField(label='Usuario :  ',required=True)
    contrasena=forms.CharField(label='Contrasena :  ',required=True,widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(

        PrependedText('usuario', '<span class="glyphicon glyphicon-user"></span>', active=True),
        PrependedText('contrasena', '<span class="glyphicon glyphicon-asterisk"></span>'),
        'multicolon_select',


    )






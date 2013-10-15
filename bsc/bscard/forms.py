#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import mision

class MisionForm(ModelForm):
    class Meta:
        model=mision
        fields = ('descripcion', 'empresa')

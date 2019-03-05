from django import forms
from .models import  School
from django.forms import ModelForm



class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ('name', 'board')
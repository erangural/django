from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView
from .models import School
from .forms import SchoolForm
# Create your views here.


class Home(ListView):
    model = School

class SchoolCreate(CreateView):
    model = School
    form_class = SchoolForm




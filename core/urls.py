from django.urls import path
from .views import Home, SchoolCreate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-school', SchoolCreate.as_view(), name='schoolcreate')
]
from django.db import models
from django.shortcuts import render, reverse

from django.db.models import Model

# Create your models here.


board = (
    ('c', 'CBSE'),
    ('i', 'ICSE'),
    ('s', 'PSEB')
)



class School(Model):
    name = models.CharField(max_length=15)
    board = models.CharField(choices=board, max_length=10)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class usuario (models.Model):
	nombre= models.CharField(max_length=30)
	apellido= models.CharField(max_length=30)
	email=models.CharField(max_length=50)
	contrasenia=models.CharField(max_length=50)

# Create your models here.

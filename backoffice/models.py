from django.db import models

# Create your models here.

class Crud(models.Model):
    nombre = models.CharField(max_length=100)
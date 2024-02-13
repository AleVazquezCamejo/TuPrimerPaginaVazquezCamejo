from django.db import models

# Create your models here.


class cliente(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
    email= models.EmailField()
    
class empleado(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
    email= models.EmailField()
    profesion = models.CharField(max_length=50)
   
class articulo(models.Model):
    nombre= models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
   
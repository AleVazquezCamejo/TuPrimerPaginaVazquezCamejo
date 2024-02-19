from django.contrib import admin
from myapp import models

# Register your models here.


admin.site.register(models.cliente)

admin.site.register(models.empleado)

admin.site.register(models.articulo)
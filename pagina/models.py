from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20, verbose_name='Usuario')
    email = models.CharField(max_length=40, verbose_name="Correo Electronico")
    password = models.Field(max_length=30, verbose_name="Contraseña")

    def __str__(self):
        return f'Usuario: {self.user} - Password: {self.password}'
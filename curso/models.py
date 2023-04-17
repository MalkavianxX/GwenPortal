from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.ImageField(upload_to='categoria/iconos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
# Create your models here.
class Curso(models.Model):
    categoria  = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    fecha = models.DateField(auto_now_add=True)
    precio = models.FloatField()
    cantidad_videos = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='curso/imagenes/', null=True, blank=True)
    usuarios_cursando = models.ManyToManyField(User, related_name='cursos_cursando', blank=True)


class Taller(models.Model):
    categoria  = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    fecha = models.DateField(auto_now_add=True)
    precio = models.FloatField()
    cantidad_videos = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='curso/imagenes/', null=True, blank=True)
    usuarios_cursando = models.ManyToManyField(User, related_name='talleres_cursando', blank=True)
   
class Video(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    fecha = models.DateField(auto_now_add=True)
    curso_pertenece = models.ForeignKey(Curso,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='curso/videos/', null=True, blank=True)

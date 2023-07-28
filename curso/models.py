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
    id_collection = models.CharField(max_length=100000,blank=True, null=True)

    def __str__(self):
        return self.nombre
class Taller(models.Model):
    categoria  = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    fecha = models.DateField(auto_now_add=True)
    precio = models.FloatField()
    cantidad_videos = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='curso/imagenes/', null=True, blank=True)
    usuarios_cursando = models.ManyToManyField(User, related_name='talleres_cursando', blank=True)
    id_collection = models.CharField(max_length=100000,blank=True, null=True)

    def __str__(self):
        return self.nombre
   
class Video(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    fecha = models.DateField(auto_now_add=True)
    curso_pertenece = models.ForeignKey(Curso,on_delete=models.CASCADE, blank=True, null=True)
    taller_pertenece = models.ForeignKey(Taller, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField(upload_to='curso/videos/', null=True, blank=True)
    link = models.CharField(max_length=10000, null=True, blank=True)
    def __str__(self):
        return self.nombre    

class Material(models.Model): 
    opciones = (
        ('word','Word'),
        ('pdf','PDF'),
        ('pp',"PowerPoint"),
        ('video',"Video"),
        ('img','Imagen'),
        ('otro','Otro')
    )
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE,blank=True, null=True)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, blank=True, null=True)
    nombre_archivo = models.CharField(max_length=1000)
    tipo_archivo = models.CharField(max_length=2000, choices=opciones)
    fecha = models.DateField(auto_now_add=True)
    archivo = models.FileField(upload_to="material/",blank=True,null=True)


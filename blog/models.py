# Create your models here.
from django.db import models

class CategoriaPost(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaPost, on_delete=models.CASCADE)
    contenido = models.TextField()
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    me_gusta = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.titulo

    def obtener_cantidad_me_gusta(self):
        return self.me_gusta.count()

# Create your models here.
from django.db import models

class CategoriaPost(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Post(models.Model):
    #general
    titulo = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaPost, on_delete=models.CASCADE)
    contenido = models.TextField()
    autor = models.CharField(max_length=255,default="Admin")
    #atributos
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    me_gusta = models.IntegerField(default=0, blank=True, null=True)
    #estilos
    estilo_color_fondo = models.CharField(max_length=1000, blank=True, null=True)
    estilo_color_letra = models.CharField(max_length=1000, blank=True, null=True)
    estilo_fuente_letra = models.CharField(max_length=1000, blank=True, null=True)
    estilo_tamano_letra_titulo = models.IntegerField(blank=True, null=True)
    estilo_tamano_letra_cuerpo = models.IntegerField(blank=True, null=True)
     
    def __str__(self):
        return self.titulo

    def obtener_cantidad_me_gusta(self):
        return self.me_gusta.count()

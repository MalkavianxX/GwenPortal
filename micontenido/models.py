from django.db import models
from django.contrib.auth.models import User
from curso.models import Curso,Taller

# Create your models here.
class MiContenido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE, blank=True, null=True)
    taller = models.ForeignKey(Taller,on_delete= models.CASCADE , blank=True, null=True)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.nombre}"
     
class ProgresoCurso(models.Model):
    inscripcion = models.ForeignKey(MiContenido, on_delete=models.CASCADE)
    porcentaje_completado = models.IntegerField(default=0)
    # Otros campos de progreso del curso, si los necesitas
    def __str__(self):
        return f"{self.inscripcion.usuario.username} - {self.inscripcion.curso.nombre}({self.porcentaje_completado}%)"   
    
class VideosVistos(models.Model):
    video_guid = models.CharField(max_length=100000)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.video_guid
class Cupones(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    cant_usado = models.IntegerField( null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.valor}"

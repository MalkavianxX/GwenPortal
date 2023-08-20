from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=10000)
    estatus = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.comentario
    
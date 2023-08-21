from django.contrib import admin
from .models import Comentario

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'comentario', 'estatus', 'fecha', 'rate')


# Registra el modelo Comentario utilizando la clase personalizada ComentarioAdmin
admin.site.register(Comentario, ComentarioAdmin)

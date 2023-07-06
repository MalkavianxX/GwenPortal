from django.contrib import admin
from .models import MiContenido, ProgresoCurso, Cupones, VideosVistos

admin.site.register(MiContenido) 
admin.site.register(ProgresoCurso)
admin.site.register(Cupones)
admin.site.register(VideosVistos)
# Register your models here.

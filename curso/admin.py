from django.contrib import admin
from .models import Categoria, Curso,Video,Taller,Material
# Register your models here.
admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(Video)
admin.site.register(Taller)
admin.site.register(Material)
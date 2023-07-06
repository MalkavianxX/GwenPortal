from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('nada-blog',views.nada, name='nada-blog'),
    path('crear_categoria',views.crear_categoria, name="crear_categoria"),
    path('get_categorias',views.get_categorias, name="get_categorias"),
    path('publicar_post',views.publicar_post, name="publicar_post"),
    path('ver_post/<int:id_post>/',views.ver_post, name="ver_post"),
    path('mostrar_blog',views.mostrar_blog, name="mostrar_blog"),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

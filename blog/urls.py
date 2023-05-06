from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('nada-blog',views.nada, name='nada-blog'),
    path('crear_categoria',views.crear_categoria, name="crear_categoria"),
    path('get_categorias',views.get_categorias, name="get_categorias"),
    path('publicar_post',views.publicar_post, name="publicar_post"),

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

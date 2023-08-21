from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('dashboard_comentarios',views.dashboard_comentarios, name='dashboard_comentarios'),

    #funciones json
    path('guardar_comentario',views.guardar_comentario, name="guardar_comentario"),
    path('aprobar_comm',views.aprobar_comm, name="aprobar_comm"),
    path('denegar_comm',views.denegar_comm, name="denegar_comm"),
    path('eliminar_comm',views.eliminar_comm, name="eliminar_comm"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

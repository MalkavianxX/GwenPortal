from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('dashboard_videos',views.dashboard_videos, name='dashboard_videos'),
    path('mostar_todos_videos',views.mostar_todos_videos, name="mostar_todos_videos"),
    path('mostrar_vtalleres',views.mostrar_vtalleres, name="mostrar_vtalleres"),
    path('mostrar_vcursos', views.mostrar_vcursos, name="mostrar_vcursos"),
    path('render_subir_video', views.render_subir_video, name="render_subir_video"),
    path('render_archivos_dash', views.render_archivos_dash, name="render_archivos_dash"),

    #URL DE JS
    path('guardar_archivo_curso', views.guardar_archivo_curso, name="guardar_archivo_curso"),
    path('guardar_archivo_taller',views.guardar_archivo_taller, name="guardar_archivo_taller"),
 
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

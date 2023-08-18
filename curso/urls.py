from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('dashboard_cursos',views.dashboard_cursos, name='dashboard_cursos'),
    path('ver_curso/<int:id_curso>/',views.ver_curso, name="ver_curso"),
    path('dashboard_talleres',views.dashboard_talleres, name="dashboard_talleres"),
    path('ver_taller/<int:id_taller>/',views.ver_taller, name="ver_taller"),
    path('guardar_curso',views.guardar_curso, name="guardar_curso"),
    path('guardar_taller', views.guardar_taller, name="guardar_taller"),
    path('public_todos_cursos',views.public_todos_cursos, name="public_todos_cursos"),
    path('render_crear_curso', views.render_crear_curso, name="render_crear_curso"),
    path('render_crear_taller', views.render_crear_taller, name="render_crear_taller"),
 
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

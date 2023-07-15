from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('login_view',views.login_view, name='login_view'),
    path('log_in',views.log_in, name="log_in"),
    path('render_dashboard',views.render_dashboard, name='render_dashboard'),
    path('register',views.register, name="register"),
    path('log_out',views.log_out, name="log_out"),
    path('render_seccion_inicio_dashboard', views.render_seccion_inicio_dashboard, name="render_seccion_inicio_dashboard"),
    path('render_seccion_blog_dashboard', views.render_seccion_blog_dashboard, name="render_seccion_blog_dashboard"),
    path('render_seccion_cursos_dashboard', views.render_seccion_cursos_dashboard, name="render_seccion_cursos_dashboard"),
    path('render_seccion_talleres_dashboard', views.render_seccion_talleres_dashboard, name="render_seccion_talleres_dashboard"),
    path('render_seccion_biblioteca_dashboard', views.render_seccion_biblioteca_dashboard, name="render_seccion_biblioteca_dashboard"),
    path('render_seccion_usuarios_dashboard', views.render_seccion_usuarios_dashboard, name="render_seccion_usuarios_dashboard"),
    path('render_seccion_mensajes_dashboard', views.render_seccion_mensajes_dashboard, name="render_seccion_mensajes_dashboard"),
    path('render_seccion_estadisticas_dashboard', views.render_seccion_estadisticas_dashboard, name="render_seccion_estadisticas_dashboard"),
    path('crear_usuario/', views.crear_usuario, name="crear_usuario"),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('dashboard_comentarios',views.dashboard_comentarios, name='dashboard_comentarios'),

 
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

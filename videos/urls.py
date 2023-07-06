from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('dashboard_videos',views.dashboard_videos, name='dashboard_videos'),
    path('mostar_todos_videos/<str:id_librari>/',views.mostar_todos_videos, name="mostar_todos_videos"),

 
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

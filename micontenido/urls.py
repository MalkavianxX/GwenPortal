from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('dash_micontenido',views.dash_micontenido, name="dash_micontenido"),
    path('agregar_al_carrito/<str:producto_id>/',views.agregar_al_carrito, name="agregar_al_carrito"),
    path('eliminar_del_carrito/<str:producto_id>/', views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path('ver_carrito/',views.ver_carrito, name="ver_carrito"),
    path('verificar_descuento/<str:cupon>/',views.verificar_descuento, name="verificar_descuento"),
    path('crear_preferencia_MP/',views.crear_preferencia_MP, name="crear_preferencia_MP"),
    path('crear_preferencia_PP',views.crear_preferencia_PP, name="crear_preferencia_PP"),
    path('pago_success/',views.pago_success, name="pago_success"),
    path('pago_danger/',views.pago_danger, name="pago_danger"),
    path('pago_pendiente/',views.pago_pendiente, name="pago_pendiente"),
    path('checkout/',views.checkout, name="checkout"),
    path('iniciar_curso/<str:id_library>/<str:id_collection>/', views.iniciar_curso,name="iniciar_curso"),
    path('marcar_completado/<str:guid>/', views.marcar_completado,name="marcar_completado"),
    path('view_change_password',views.view_change_password, name="view_change_password"),
    path('fun_change_password',views.fun_change_password, name="fun_change_password"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# vet_sprint/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL
    path('', views.home, name='home'),
    path('servicios/', views.services, name='services'),
    path('informacion/', views.dynamic_content_placeholder, name='dynamic_placeholder'), # Ajustado el nombre de la URL

    # URL Propietarios
    path('propietarios/', views.propietarios_list, name='propietarios_list'),
    path('propietarios/crear/', views.propietario_create, name='propietario_create'),
    path('propietarios/actualizar/<int:pk>/', views.propietario_update, name='propietario_update'),
    path('propietarios/eliminar/<int:pk>/', views.propietario_delete, name='propietario_delete'),

    # URL Mascotas
    path('mascotas/', views.mascotas_list, name='mascotas_list'),
    path('mascotas/crear/', views.mascota_create, name='mascota_create'),
    path('mascotas/actualizar/<int:pk>/', views.mascota_update, name='mascota_update'),
    path('mascotas/eliminar/<int:pk>/', views.mascota_delete, name='mascota_delete'),

    # URL Citas
    path('citas/', views.citas_list, name='citas_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    path('citas/actualizar/<int:pk>/', views.cita_update, name='cita_update'),
    path('citas/eliminar/<int:pk>/', views.cita_delete, name='cita_delete'),
]
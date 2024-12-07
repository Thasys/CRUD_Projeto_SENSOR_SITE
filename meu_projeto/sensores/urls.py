from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # A URL raiz é mapeada para a view 'home'
    path('create/', views.create_sensor, name='create_sensor'),
    path('list/', views.list_sensors, name='list_sensors'),
    path('update/<uuid:sensor_id>/', views.update_sensor, name='update_sensor'),
    path('delete/<uuid:sensor_id>/', views.delete_sensor, name='delete_sensor'),
    path('<uuid:sensor_id>/create_leitura/', views.create_leitura, name='create_leitura'),
    path('<uuid:sensor_id>/list_leituras/', views.list_leituras, name='list_leituras'),
]

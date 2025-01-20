from django.urls import path
from . import views # o ponto significa "importar do diretório base do arquivo"

urlpatterns = [
    path('', views.index, name="Index"),
    path('staff/', views.staff, name="Staff")
]

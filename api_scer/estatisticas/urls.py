from django.urls import path
from . import views # o ponto significa "importar do diretório base do arquivo"

urlpatterns = [
    path('estatisticas/', views.index, name="estatisticas-index"),
    path('staff/', views.staff, name="estatisticas-staff"),
    path('produtos/', views.produtos, name="estatisticas-produtos"),
    path('retirada/', views.retirada, name="estatisticas-retirada"),
]

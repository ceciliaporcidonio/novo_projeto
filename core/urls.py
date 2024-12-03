from django.urls import path
from . import views  # Importa as views do app core

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('async-counter/', views.async_counter, name='async_counter'),  # Nova rota para o contador
]


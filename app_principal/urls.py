from django.urls import path
from . import views

urlpatterns = [
    path('', views.cria_mensagem, name="enviar_mensagem"),
    path('login/', views.valida_login_adm, name="valida_login"),
    path('lista_mensgens/', views.lista_mensagens, name="lista_mensagens"),
]

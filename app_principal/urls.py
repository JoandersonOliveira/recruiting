from django.urls import path
from . import views

urlpatterns = [
    path('', views.enviar_mensagem, name="enviar_mensagem"),
    path('login/', views.valida_usuario, name="valida"),

]

from django.contrib import admin
from .models import Mensagem

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'mensagem', 'lido', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem', 'lido', 'data_envio')


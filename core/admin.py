# admin.py
from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'status')
    list_filter = ('status',)
    search_fields = ('nome', 'cpf')

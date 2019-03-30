from django.contrib import admin
from .models import Agenda, Pessoa, TipoAgenda, Compromisso

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoAgenda)
class TipoAgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(Compromisso)
class CompromissoAdmin(admin.ModelAdmin):
    pass


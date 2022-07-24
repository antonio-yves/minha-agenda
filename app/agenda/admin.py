"""
    Registro dos models no Django Admin
"""

from django.contrib.admin import site, ModelAdmin
from django.utils.translation import gettext as _
from app.agenda.models import Compromisso


class CompromissoAdmin(ModelAdmin):

    list_display = (
        'nome_compromisso',
        'data',
        'hora_inicio',
        'hora_termino',
        'status_compromisso',
    )
    search_fields = (
        'nome_compromisso',
        'data',
        'status_compromisso',
    )
    fieldsets = (
        (
            _('Detalhes do Compromisso'),
            {
                'fields': (
                    'nome_compromisso',
                    'data', 'hora_inicio',
                    'hora_termino', 'local',
                    'observacoes',
                    'status_compromisso'
                )
            }
        ),
    )


site.register(Compromisso, CompromissoAdmin)

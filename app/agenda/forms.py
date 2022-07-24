"""
    Forms utilizados na aplicação
"""

from django import forms
from app.agenda.models import Compromisso


class CompromissoForm(forms.ModelForm):
    """Form responsável pelo cadastro e atualização de um Compromisso"""
    class Meta:
        model = Compromisso
        fields = (
            'nome_compromisso',
            'data',
            'hora_inicio',
            'hora_termino',
            'local',
            'observacoes',
            'status_compromisso',
        )
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d"),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}, format="%H:%M"),
            'hora_termino': forms.TimeInput(attrs={'type': 'time'}, format="%H:%M"),
            'observacoes': forms.Textarea(attrs={'rows': 5}),
        }

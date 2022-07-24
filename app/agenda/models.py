"""
    Models da aplicação
"""

from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class Compromisso(models.Model):
    """Model de Compromisso"""
    STATUS = (
        ('A', _('Agendado')),
        ('C', _('Cancelado')),
        ('R', _('Realizado')),
    )

    # Atributos de Compromisso
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='usuario', blank=False
    )
    nome_compromisso = models.CharField(
        _('Nome do compromisso'), max_length=120, blank=False
    )
    data = models.DateField(
        _('Data'), blank=False, auto_now_add=False
    )
    hora_inicio = models.TimeField(
        _('Hora de início'), blank=False, auto_now_add=False
    )
    hora_termino = models.TimeField(
        _('Hora de término'), blank=False, auto_now_add=False
    )
    local = models.CharField(
        _('Local'), max_length=120, blank=False
    )
    observacoes = models.TextField(
        _('Observações'), blank=True, null=True
    )
    status_compromisso = models.CharField(
        _('Status do compromisso'), max_length=1, choices=STATUS, default='A'
    )

    def __str__(self) -> str:
        return self.nome_compromisso

    class Meta:
        verbose_name = _('Compromisso')
        verbose_name_plural = _('Compromissos')
        db_table = 'compromissos'

"""
    Classes abstratas que contêm as regras de negócio da aplicação
"""

from abc import ABC
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from app.agenda.models import Compromisso
from app.agenda.exceptions import ConflitoDeHorario
from datetime import datetime


class ValidaChoqueDeHorario(ABC):
    """
    Classe abstrata que trata o conflito de horário entre os compromissos
    cadastrados do usuário.
    """
    def form_valid(self, form):
        try:
            if 'pk' in self.kwargs:
                compromissos = Compromisso.objects.filter(
                    data=datetime.strptime(
                        form.data.get('data'), '%Y-%m-%d'
                    ).date()
                ).exclude(pk=self.kwargs['pk'])
            else:
                compromissos = Compromisso.objects.filter(
                    data=datetime.strptime(
                        form.data.get('data'), '%Y-%m-%d'
                    ).date()
                )

            hora_inicio = datetime.strptime(form.data.get('hora_inicio'), '%H:%M').time()
            hora_termino = datetime.strptime(form.data.get('hora_termino'), '%H:%M').time()

            for compromisso in compromissos:
                if (compromisso.hora_inicio <= hora_inicio <= compromisso.hora_termino or
                    compromisso.hora_inicio <= hora_termino <= compromisso.hora_termino or
                    (hora_inicio < compromisso.hora_inicio and hora_termino > compromisso.hora_termino)):
                    raise ConflitoDeHorario(f'Choque de horário com o compromisso: <b>{compromisso.nome_compromisso}</b>!')
        except ConflitoDeHorario as ex:
            messages.add_message(self.request, messages.ERROR, ex.mensagem)
            return render(self.request, self.template_name, {'form': form})
        else:
            if 'pk' in self.kwargs:
                messages.add_message(self.request, messages.SUCCESS, 'Compromisso atualizado!')
            else:
                messages.add_message(self.request, messages.SUCCESS, 'Compromisso adicionado a sua agenda!')
            form.instance.usuario = self.request.user
            return super().form_valid(form)

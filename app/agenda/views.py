"""
    Views da aplicação
"""

import os
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import FileResponse
from django.core.exceptions import EmptyResultSet
from django.conf import settings
from app.agenda.models import Compromisso
from app.agenda.forms import CompromissoForm
from app.agenda.bussines import ValidaChoqueDeHorario
from app.agenda.functions import gera_csv, gera_excel


class AdicionarCompromissoView(LoginRequiredMixin, ValidaChoqueDeHorario, CreateView):
    """View responsável por adicionar um novo compromisso"""
    model = Compromisso
    template_name: str = 'agenda/adicionar.html'
    form_class = CompromissoForm
    success_url = reverse_lazy('app.agenda:home')


class DetalhesCompromissoView(LoginRequiredMixin, DetailView):
    """View responsável por exibir os detalhes de um compromisso"""
    model = Compromisso
    template_name: str = 'agenda/detalhes.html'


class EditarCompromissoView(LoginRequiredMixin, ValidaChoqueDeHorario, UpdateView):
    """View responsável por editar os dados de um compromisso"""
    model = Compromisso
    template_name: str = 'agenda/editar.html'
    form_class = CompromissoForm
    success_url = reverse_lazy('app.agenda:home')


class ExcluirCompromissoView(LoginRequiredMixin, DeleteView):
    """View responsável por realizar a exclusão de um compromisso"""
    model = Compromisso
    success_url = reverse_lazy('app.agenda:home')

    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, f'O compromisso <b>{self.get_object().nome_compromisso}</b> foi removido com sucesso!')
        return super().delete(request, *args, **kwargs)


class ExportarDadosView(LoginRequiredMixin, View):
    """View responsável por exportar os compromissos do usuário"""
    template_name = 'agenda/exportar.html'
    queryset = Compromisso.objects.all()

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            nome_arquivo = None
            queryset = self.queryset.filter(usuario=request.user)
            if request.POST.get('tipo_arquivo') == '1':
                nome_arquivo = gera_csv(queryset)
            else:
                nome_arquivo = gera_excel(queryset)
            arquivo = open(os.path.join(settings.BASE_DIR, f'media/temp/{nome_arquivo}'), 'rb')
            return FileResponse(arquivo, as_attachment=True)
        except EmptyResultSet:
            messages.add_message(request, messages.ERROR, 'Não há compromissos para serem exportados!')
            return render(request, self.template_name)


class HomeView(LoginRequiredMixin, ListView):
    """View principal, onde é exibido os compromissos do usuário em forma de calendário e lista"""
    model = Compromisso
    template_name: str = 'agenda/calendario.html'

    def get_queryset(self):
        queryset = Compromisso.objects.filter(usuario=self.request.user)
        if len(self.request.GET.dict()) != 0:
            queryset = queryset.filter(
                nome_compromisso__icontains=self.request.GET.get('nome_compromisso'),
                local__icontains=self.request.GET.get('local')
            )
            if self.request.GET.get('data_inicial') != '':
                queryset = queryset.filter(
                    data__gte=self.request.GET.get('data_inicial')
                )
            if self.request.GET.get('data_final') != '':
                queryset = queryset.filter(
                    data__lte=self.request.GET.get('data_final')
                )
            if self.request.GET.get('hora_inicial') != '':
                queryset = queryset.filter(
                    hora_inicio__gte=self.request.GET.get('hora_inicial')
                )
            if self.request.GET.get('hora_final') != '':
                queryset = queryset.filter(
                    hora_termino__lte=self.request.GET.get('hora_final')
                )
            if self.request.GET.get('status_compromisso') != '':
                queryset = queryset.filter(
                    status_compromisso=self.request.GET.get('status_compromisso')
                )
        return queryset

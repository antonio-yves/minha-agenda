"""
    URLs da aplicação
"""

from django.urls import path
from app.agenda.views import *


app_name = 'app.agenda'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('compromisso/novo/', AdicionarCompromissoView.as_view(), name='novo_compromisso'),
    path('compromisso/<pk>/detalhes/', DetalhesCompromissoView.as_view(), name='detalhes_compromisso'),
    path('compromisso/<pk>/editar/', EditarCompromissoView.as_view(), name='editar_compromisso'),
    path('compromisso/<pk>/excluir/', ExcluirCompromissoView.as_view(), name='excluir_compromisso'),
    path('compromissos/exportar/', ExportarDadosView.as_view(), name='exportar_dados'),
]

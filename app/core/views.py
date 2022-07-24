"""
    Views da aplicação
"""

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from app.core.forms import CadastrarUsuarioForm


class CadastrarUsuarioView(CreateView):
    """View responsável por realizar o cadastro de um usuário"""
    model = User
    template_name: str = 'core/registro.html'
    success_url = reverse_lazy('app.core:login')
    form_class = CadastrarUsuarioForm

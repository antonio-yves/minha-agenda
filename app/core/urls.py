"""
    URLs da aplicação
"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app.core.views import CadastrarUsuarioView


app_name = 'app.core'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', CadastrarUsuarioView.as_view(), name='cadastro'),
]

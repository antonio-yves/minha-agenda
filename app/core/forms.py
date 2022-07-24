"""
    Forms utilizados na aplicação
"""

from django import forms
from django.contrib.auth.models import User


class CadastrarUsuarioForm(forms.ModelForm):
    """Form responsável pelo cadastro de novos Usuários"""
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'password': forms.PasswordInput(attrs={'type': 'password'}),
        }
"""
    Exceções personalizadas para a aplicação atual.
"""


class ConflitoDeHorario(Exception):
    """Um erro enquanto um novo Compromisso está sendo cadastrado."""
    def __init__(self, mensagem):
        """
        O argumento mensagem pode ser utilizado para explicar ao usuário
        que o Compromisso que ele está tentando cadastrar tem choque de
        horário com um já existente.
        """
        self.mensagem = mensagem

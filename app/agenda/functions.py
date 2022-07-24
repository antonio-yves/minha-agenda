"""
    Funções utilizadas na aplicação
"""

import os, xlsxwriter, csv
from django.core.exceptions import EmptyResultSet
from django.conf import settings
from datetime import datetime


def gera_csv(queryset):
    """Função responsável por gerar a exportação dos dados em CSV"""
    if len(queryset) == 0:
        raise EmptyResultSet

    data_hora_atual = datetime.now()
    nome_arquivo = f"exportacao_{data_hora_atual.strftime('%Y%m%d%H%M%S')}.csv"

    with open(os.path.join(settings.BASE_DIR, f'media/temp/{nome_arquivo}'), 'w', newline='', encoding='utf-8') as relatorio:
        # Cabeçalho do arquivo
        csv.writer(relatorio, delimiter=',').writerow(['Nome do compromisso', 'Data', 'Hora de início', 'Hora de término', 'Local', 'Status compromisso', 'Observações'])

        # Conteúdo
        for compromisso in queryset:
            csv.writer(relatorio, delimiter=',').writerow([
                compromisso.nome_compromisso,
                compromisso.data,
                compromisso.hora_inicio,
                compromisso.hora_termino,
                compromisso.get_status_compromisso_display(),
                compromisso.observacoes,
            ])
    return nome_arquivo


def gera_excel(queryset):
    """Função responsável por gerar a exportação dos dados em Excel"""
    if len(queryset) == 0:
        raise EmptyResultSet

    data_hora_atual = datetime.now()
    nome_arquivo = f"exportacao_{data_hora_atual.strftime('%Y%m%d%H%M%S')}.xlsx"

    workbook = xlsxwriter.Workbook(os.path.join(settings.BASE_DIR, f'media/temp/{nome_arquivo}'))
    worksheet = workbook.add_worksheet("Compromissos exportados")

    # Cabeçalho do arquivo
    worksheet.write(0, 0, 'Nome do compromisso')
    worksheet.write(0, 1, 'Data')
    worksheet.write(0, 2, 'Hora de início')
    worksheet.write(0, 3, 'Hora de término')
    worksheet.write(0, 4, 'Local')
    worksheet.write(0, 5, 'Status compromisso')
    worksheet.write(0, 6, 'Observações')

    linha = 1
    for compromisso in queryset:
        worksheet.write(linha, 0, compromisso.nome_compromisso)
        worksheet.write(linha, 1, compromisso.data.strftime('%d/%m/%Y'))
        worksheet.write(linha, 2, compromisso.hora_inicio.strftime('%H:%M'))
        worksheet.write(linha, 3, compromisso.hora_termino.strftime('%H:%M'))
        worksheet.write(linha, 4, compromisso.local)
        worksheet.write(linha, 5, compromisso.get_status_compromisso_display())
        worksheet.write(linha, 6, compromisso.observacoes)
        linha += 1

    workbook.close()
    return nome_arquivo

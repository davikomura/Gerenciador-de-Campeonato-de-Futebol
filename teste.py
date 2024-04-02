# -*- coding: utf-8 -*-
"""
@author: Davi Komura
"""

from simulador_campeonato import imagem_df

# Definindo a força de cada time
times = [
    {'Time': 'Corinthians', 'Nível': '10'},
    {'Time': 'Palmeiras', 'Nível': '5'},
    {'Time': 'São Paulo', 'Nível': '2'},
    {'Time': 'Santos', 'Nível': '8'},
    {'Time': 'Flamengo', 'Nível': '8'},
    {'Time': 'Vasco', 'Nível': '6'}
]

# Gerando a imagem da tabela
imagem_df(times, 'output_teste.png')

print("Tabela de classificação gerada com sucesso! Verifique o arquivo output_teste.png.")


# Definindo Funções em Python

# DRY - Don't Repeat Yourself / Não Repita Você Mesmo(ou Seu Código)

# É o conceito de repetir menos vezes possível o seu código

"""
# Cara ou Coroa
def moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    else:
        return 'Coroa'

print(moeda())

"""

# Em um Função ter diferentes "return"s

from random import random

# Pedra Papel ou Tesoura

def pedra_papel_tesoura():
    valor = random()
    print(valor)

    if valor < 0.3:
        return 'Pedra'
    elif valor > 0.3 and valor < 0.7:
        return 'Papel'
    else:
        return 'Tesoura'

print(pedra_papel_tesoura())

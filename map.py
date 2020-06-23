'''
Map

Com map, fazemos mapeamento dos valores para a função. # Realiza uma determinada função em qualquer item,
desde que seja iterável.
Map Recebe dois parâmetros: Uma função e um iterável

import math


def area(r): # Uma função comum
    """Calcula a área de um círculo com raio 'r'."""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
resutaldo = []

# Forma 1
for r in raios: # Realizando o calculo do raio de toda uma lista
    resutaldo.append(area(r)) # Resultado adicionado em uma lista
print(resutaldo)

# Utilizando o map

strings = ['1','8','9','15','9','7']

meta = map(int,strings) # Converte os itens da lista em Inteiros
meta = list(meta) # A função Map retorna um objeto, por isso precisamos especificar seu tipo
print(meta)

# Forma 2
dados = map(area, raios)
print(list(dados))

# Forma 3 - Utilizando lambdas

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Depois da execução de um objeto 'map' ele o apaga, deixando assim a memória mais 'limpa'.
'''

# Forma 4 - Utilizando Lambdas

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles, 26'), ('Tokio', 27)]

c_to_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_to_f, cidades)))

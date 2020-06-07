'''
Segue o mesmo conceito de list_Comprehensions

# Sintaxe = {chave:valor (operação) for chave, valor in iterável}

# Exemplo 1
numeros = {'a':1, 'b':2, 'c':3, 'd':4}

dobro = {chave: valor * 2 for chave,valor in numeros.items()}
print(dobro) # Dobra os valores de cada chave do dicionário

# Exemplo 2
numeros = [1, 2, 3, 4]

dobro = {valor: valor * 2 for valor in numeros}
print(dobro)

# Exemplo 3 - Utilizando duas listas para criar um dicionário

chaves = ['daniel', 'Sonia', 'Lais', 'Manoel', 'End']
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo 3 - Utilizando estrutura condicional

numeros = [1, 2, 3, 4]
res = {chaves:('Par' if chaves % 2 == 0 else 'Impar')for chaves in numeros}
print(res)
'''



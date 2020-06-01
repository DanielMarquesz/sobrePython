'''

List Comprehesions

- Utilizando LC nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe

[dado for dado in dados]


# Exemplo 1

numeros = [12, 32, 45 , 4]

res = [numero * 10 for numero in numeros]
print(res)

# podemos ver que a LC trabalha de duas formas, em sua estruturas
# Onde na primeira parte 'numero * 10' é realizada alguma ação
# Já na Segunda a lista é percorrida normalmente realizando tal ação

# Exemplo 2

res = [numero/2 for numero in numeros]
print(res)

# Exemplo 3

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)

# List Comprehensions VS Loops

# Loop Comum

numeros = [2, 3, 6, 8]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# List Comprehensions

print([numero * 2 for numero in numeros])

# List Comprehensions VS Loops

# Loop Comum

numeros = [2, 3, 6, 8]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# List Comprehensions

print([numero * 2 for numero in numeros])

'''
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

# Mais Exemplos

# Exemplo 1 - Poem a primeira letra dos nomes da lista como maiúsculo

nomes = ['daniel' ,'marques']
print([caixa_alta(nome) for nome in nomes])


# Exemplo 2 - Coloca todas as letras de uma variável como maiúsculas

palavra = 'abacate'
print([letra.upper() for letra in palavra])


# Exemplo 3 - Multiplica os números em determinado intervalo

print([numero * 3 for numero in range(1,8)])

# Exemplo 4 - Mostra o valor lógico dos itens na lista

print([bool(valor) for valor in [0, [], '', 1, True, 3.14]])

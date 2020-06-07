'''
Listas Aninhadas

- Algumas linguages de programação possuem uma estrutura de dados chamada de "array" ou "vetor".
    Essas estruturas podem ser classificadas como:
        - Unidimensionais (Arrays / Vetores)
        - Multidimensionais (Matrizes)

Em Python temos listas, que são bem mais flexiveis.

numeros = [2,'b',2.18,True]

# Exemplo 1

# 1,2,3
# 4,5,6
# 7,8,9
listas = [[1,2,3],[4,5,6],[7,8,9]] # Lista 3x3

print(listas[1]) # saida [4, 5, 6]
print(listas[1][2]) # saida 6 - linha 1 coluna 2

# Exemplo 2

# - Iteração com loops em uma lista aninhada
for lista in listas: # mostra cada linha
    for num in lista: # mostra os itens da lista
        print(num)

listas = [[1,2,3],[4,5,6],[7,8,9]] # Lista 3x3

# iteração com List Comprehension

[[print(valor) for valor in lista] for lista in listas] # mostra todos os itens da lista


# Gerando um tabuleiro/matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O'for numero in range(1, 4)]for valor in range(1, 4)]
print(velha) # Os houverem números pares haverão Xs

# Gerando valores iniciais
valores = [0 for vazio in range(1,4)]
print(valores[0])
'''

'''
Set Comprehension

Lista = [1, 2, 3, 4]
Conjunto = {1, 2, 3, 4}
'''
# Exemplo 1
print({num for num in range(1, 6)}) # Imprime números no intrvalo

# Exemplo 2
print({x**2 for x in range(1, 6)}) # Faz uma operação com os números no intervalp

# Exemplo 3
idades = ['Daniel','Sonia','Manoel','Laís','Thaís']
numeros = {idades[x]: x ** 2 for x in range(0,5)} # Adicionando Itens a um dicionário
print(numeros)

# Exemplo 4 - Impressão de Strings

letras = {letras for letras in 'Daniel Marques'}
print(letras) # Imprime as letras da string sem repetições e sem ordenação

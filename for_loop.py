"""
Estrutura de Repetição For



nome = 'Daniel'
lista = [1,2,6,8,10]
numeros = range (1,10)

 Iterando uma String
for letra in nome:
    print(letra)

 Iterando uma lista
for numero in lista:
    print(numero)

 Iterando um Range
for range in numeros:
    print(range)

curso = "Geek University"
print(curso[5:15])

qnt = int(input("Quantas repetições? "))

for i in range (1, qnt+1):
    print(f"Repetição N° {i}")

    qnt = int(input('Quantas Vezes esse Loop deve Rodar?'))
soma = 0

for i in range (1, qnt + 1):
    num = int(input(f'Insira o valor {i}/{qnt}: '))
    soma = num + soma
print(soma,end='')


qnt = int(input("Quantas repetições? "))

for i in range (1, qnt+1):
    print(f"Repetição N° {i}")

"""

# Loop com posições já inseridas

pessoas = ['Pedro','Thiago','João','Barquinho']
n = 0
for i in range(len(pessoas)):
    print(f'O sujeito {i} está na posição: {pessoas[i]}')
    n += 1

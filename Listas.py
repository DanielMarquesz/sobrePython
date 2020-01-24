'''
Listas em Python são a mesma coisa do que vetores em outras linguagens
As principais diferenças entre as Listas em Python e os vetores em outras linguagens
é a de que as Listas em python são dinâmicas. Em java por exemplo um vetor
precisa ter declarado seu tipo(int,double,boolean) e seu tamanho, enquanto que no python
pode ser inserido qualquer tipo de dado, numeros, strings, arquivos... e podem ser adiciona-
dos itens até que sua memória RAM seja totalmente preechida.


====================================================================================================

nome = list('Daniel Marques')

lista = [ 10, 10 ,230 ,210, 23]
vetor = list('Daniel Marques')
#print(lista[4])
#print(lista[5])
#print(pedro)

#Verificando se um valor esta em uma lista
if 23 in lista:
    lista.sort()
    print(lista)
else:
    print('não esta aqui')

#número de Ocorrências em uma lista,
print(lista.count(10))
print(vetor.count('e'))

#Adicionando Elementos em listas

lista.append(32)
print(lista)

#Adiciona a lista como uma sublista
lista.append([23,87,8])
print(lista)

if [23,87,8] in lista:
    print('Encontrei a Lista! ')
else:
    print('Não encontrei a Lista! ')

# Adiciona os arquivos da sublista a lista indicada
lista.extend([658,67])
print(lista)

# Podemos inserir um novo elemento na lista informando a posição do índice
# Não substitui nenhum valor
lista1.insert(3 ,'Novo valor')
print(lista1)

# Podemos Facilmente Juntar duas listas
lista6 = (lista1 + lista2)
print(lista6)

# Mostra o tamanho(elementos) de Uma lista
print(len(lista1))

# Remove e retorna o último elemento
print(lista1)
lista1.pop()
print(lista1)

# Podemos remover um elemento de uma lista através da sua posição
lista2.pop(1)
print(lista2)

# Podemos Inverter uma lista
lista1.reverse()
lista2.reverse()

print(lista2)
print(lista1)

# Removento todos os elementos de uma lista

print(lista5)
lista5.clear()
print(lista5)

# Transformando uma string em lista

# Exemplo 1

nome = 'Daniel da Conceição Marques'
nome = nome.split()
print(nome)

# Exemplo 2

doce = 'bananada'
doce = doce.split('a')
print(doce)


# Transformando uma string em lista

# Exemplo 1

nome = 'Daniel da Conceição Marques'
nome = nome.split()
print(nome)

# Exemplo 2

doce = 'bananada'
doce = doce.split('a')
print(doce)

# Transformando uma lista em string

do = ''.join(doce)
print(do)

# Iterando sobre listas

#Exemplo 1 - Utilizando For
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print('Total:', soma)

#Exemplo 2 - Utilizando o While

carrinho = []
produto = ''

while produto != 'sair':
    print('Digite um produto para adicionar a lista ou digite "sair" para sair')
    produto = input()

    if produto != 'sair':
        carrinho.append(produto)


for produto in carrinho:
    print(produto)


# loop para acessar as cores em um vetor

cores = ["amarelo","azul","verde","laranja"]
#Ex:1
for cor in cores:
    print(cor)

#Ex:2
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


# Gerando índice em um vetor

cores = ['azul','amarelo','vermelho','preto']

for indice, cor in enumerate(cores):
    indice = indice + 1
    print(indice, cor)

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 6, 9, 10]

print('Em qual número da linha está o valor 6? ')
print(numeros.index(6))

print('Em qual número da linha está o valor 10? ')
print(numeros.index(10))

# Revisão de Slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Como funciona o parâmetro Início
lista = [1,2,3,4,6,8]
print(lista[2:])

# Como funciona o parâmetro FIM

print(lista[:5])


# Invertendo Valores de Uma Lista

nome = ['Daniel','Marques']

nome[0], nome[1] = nome[1], nome[0]

print(nome)
nome.reverse()
print(nome)

# Soma*, maximo*, mínimo*, tamanho

# só funciona com números inteiros ou reais

lista =[1,2,3,4,5,6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transformar uma lista em Tupla

lista = [1,2,3,4,5,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1,2,3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

'''
lista1 = [1,88,54,323,54,87,60]

lista2 = ['L','a','i','s']

lista3 = []

lista4 = [list(range(11))]

lista5 = [list('Daniel Marques')]

# Copiando uma lista para outra (Shalow Copy e Deep Copy)

# Veja que quando realizamos a cópia da lista, geramos uma nova, totalmente independente. Ou seja, ela não interfere
# na original, isso em python é chamado de Deep Copy.

# Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Forma 2 - Shalow Copy

# Faz a cópia utilizando método de atribuição, e o que for alterado na nova lista copiada,
# altera o valor também na lista original.

lista = [1, 2, 3]
print(lista)

nova = lista #cópia

nova.append(4)

print(nova)
print(lista)

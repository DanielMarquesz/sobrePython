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

'''
lista1 = [1,88,54,323,54,87,60]

lista2 = ['L','a','i','s']

lista3 = []

lista4 = [list(range(11))]

lista5 = [list('Daniel Marques')]

# Podemos inserir um novo elemento na lista informando a posição do índice
# Não substitui nenhum valor

#lista1.insert(3 ,'Novo valor')
#print(lista1)

# Podemos Facilmente Juntar duas listas
lista6 = (lista1 + lista2)
print(lista6)


print(lista1.sort())




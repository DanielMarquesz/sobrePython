'''
Listas em Python são a mesma coisa do que vetores em outras linguagens
As principais diferenças entre as Listas em Python e os vetores em outras linguagens
é a de que as Listas em python são dinâmicas. Em java por exemplo um vetor
precisa ter declarado seu tipo(int,double,boolean) e seu tamanho, enquanto que no python
pode ser inserido qualquer tipo de dado, numeros, strings, arquivos... e podem ser adiciona-
dos itens até que sua memória RAM seja totalmente preechida.

'''
nome = list('Daniel Marques')

lista = [ 10, 10 ,230 ,210, 'oi', 'olá','www.google.com.br']
#print(lista[4])
#print(lista[5])
#print(pedro)

#Verificando se um valor esta em uma lista

if 'a' in nome:
    print('esta aqui')
else:
    print('não esta aqui')

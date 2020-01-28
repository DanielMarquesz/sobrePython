"""
Tuplas -

São parecidas com listas, porém elas:

 - São compostas por "( )"
 - Tuplas são imutáveis: Ao se criar uma tupla ela não muda, toda operação em uma tupla gera uma nova tupla.
 - Não é possível Adicionar ou Remover valores nas tuplas

 # Por que Utilizar Tuplas? (Trabalhar com elementos imutáveis traz segurança para o código)

 - Tuplas são mais rápidas do que listas
 - Tuplas deixam seu código mais seguro


# Exemplos de tuplas

# Ex1:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Ex2:

tupla3 = (1)  # Tuplas são definidas pelo uso de vírdulas,ao invés de parenteses
print(tupla3)

print(type(tupla3))

#Podemos gerar uma tupla com o range()
tupla = tuple(range(10))
print(tupla)

print(type(tupla))
# Desempacotamento de Tuplas

tupla = ('Daniel Marques','Lais Alves')
homem, mulher = tupla

print(homem)
print(mulher)

# Soma, Valor Máximo, Valor Mínimo e Tamanho de Tuplas
# Somente para valores inteiros
tupla = (1.6,2,3,4,8,5)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de Tuplas
tupla1 = (1,2,3)
print(tupla1)

tupla2 = (4,5,6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

# Verificar se um elemento está em determinada tupla
tupla = (range(10))

print(8 in tupla)

# Iterando sobre uma Tupla

tupla = (range(6))
n = 0
for i in tupla:
    print(i)

# Contato elementos dentro de uma tupla
tupla = ('a','a','b','b','c','d','e')
print(tupla.count('e'))

word = tuple('Daniel da Conceiçao Marques')
print(word.count('a'))

# Devemos sempre utilizar uma tupla quando não precisarmos modificar os dados contidos nelas

# Exemplo:

meses = ('JANEIRO','FEVEREIRO','MARCO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO')
# Não existe sentido em adicionar ou remover os meses do ano.

# O Acesso aos elementos das tuplas é feita de maneira semelhante a das listas

print('Eu faço Aniversário em' ,meses[8])

# Iterando com o While
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificando em qual índice um elemento está na tupla
print(meses.index('SETEMBRO',8))

# Slicing
# Tupla[inicio:fim:passo]
print(meses[0:3])
"""









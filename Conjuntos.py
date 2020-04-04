'''

Conjuntos

- Em toda linguagem de programação o que estudamos na matemática sobre teoria dos conjuntos é válido
- Em Python Conjuntos são chamados de Sets.

Da mesma forma que na matemática:

- Sets(Conjuntos), não possuem valores duplicados
- Sets(Conjuntos), não possuem valores ordenados
- Elementos não são acessados via índice

Conjuntos são ideais para se usar quando precisamos utilizar elementos
mas não nos importamos com a ordenação deles, quando não precisamos nos preocupar
com chaves, valores e itens duplicados.

Os conjuntos(Sets) são referenciados em Pytho através de "{}"

Diferença entre conjuntos (Set) e Mapas(Dicionários) em Python:
    - Um dicionário tem chave valor;
    - Um conjunto tem apenas valor;

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 4, 7, 1, 1})
print(type(s))
print(s)

# Caso seja adicionado um valore repetido, o Set ignora esse valor

# Forma 2 - mais comum

s = {1,2,3,4,5,5}
print(s)

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print("Lista: ", lista, "com",len(lista), "elementos")

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = tuple([99, 2, 34, 23, 2, 12, 1, 44, 5, 34])
print("Tupla: ", tupla, "com",len(tupla), "elementos")

# dicionarios aceitam valores duplicados, mas não aceitam valores de chaves duplicados, logo possuem 8 chaves
dicionario = {}.fromkeys(lista, 'Dict')
print("Dicionário: ", dicionario, "com",len(dicionario), "elementos")

# Conjuntos não aceitam elementos repetidos, ele simplesmente os ignora, possuem 8 elementos
conjunto = set(lista)
print("Conjunto: ", conjunto, "com",len(conjunto), "elementos")


cidade = ['itaboraí','Rio de janeiro','São Paulo','Cúiaba','itaboraí']

print(cidade)
print(set(cidade)) # Remove os elementos repetidos da lista e transforma em um conjunto

# Adicionando Elemento em Um Conjunto

conjunto = {'daniel','23',23}
conjunto.add(24)
print(conjunto)

# Removendo Elemento em Um Conjunto

conjunto = {'daniel','23',23}
conjunto.remove('daniel')
print(conjunto)


# Forma2 - Removendo Elemento em Um Conjunto

conjunto = {'daniel','23',23}
conjunto.discard('daniel')  # se o valor não for encontrado nenhum erro é gerado
print(conjunto)


# Apagando todos os dados de um conjunto

conjunto = {'daniel','23',23}
conjunto.clear()
print(conjunto)


estudantesPython = {'Marcos','Patricia','Ellen','Pedro','Julia','Guilherme'}
estudantesJava = {'Fernando','Gustavo','Julia','Ana','Patricia'}


# Forma 1 - União entre conjuntos - "Union"

unicos1 = estudantesPython.union(estudantesJava)
print(unicos1)
# Resultado - Sem Repetições
#{'Gustavo', 'Ellen', 'Guilherme', 'Ana', 'Julia', 'Pedro', 'Patricia', 'Marcos', 'Fernando'}


# Métodos Matemáticos de Conjuntos

estudantesPython = {'Marcos','Patricia','Ellen','Pedro','Julia','Guilherme'}
estudantesJava = {'Fernando','Gustavo','Julia','Ana','Patricia'}
estudantePerl = {'Daniel','Moraes','Costa'}

# Forma 2 - Utilizando o Caractere Pipe

unicos = estudantesPython | estudantesJava | estudantePerl
print(unicos)


estudantesPython = {'Marcos','Patricia','Ellen','Pedro','Julia','Guilherme'}
estudantesJava = {'Fernando','Gustavo','Julia','Ana','Patricia'}
estudantePerl = {'Daniel','Moraes','Costa'}

# Gerar um conjunto com os alunos que estão em ambos os cursos

# 1 Forma - Utilizando Intersection

ambos = estudantesPython.intersection(estudantesJava)
print(ambos)

# 2 Forma Utilizando &

ambos1 = estudantesPython & estudantesJava
print(ambos1)

# Gerar um Conjunto de estudantes que não estão no outro

onlyPython = estudantesJava.difference(estudantesPython)
print(onlyPython)

onlyJava = estudantesPython.difference(estudantesJava, estudantePerl)
print(onlyJava)




'''







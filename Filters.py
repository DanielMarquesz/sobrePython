"""
Filter - Server para Filtrar uma determinada coleção de dados:Dicts, Lists, Tuples.
Filter - Usualmente só retona valores com status "True".

import statistics

# Exemplo - 1

dados = [1.3, 2.5, 3, 6, 8.8, 9]

media = statistics.mean(dados) # Função importada que retorna a média de um conjunto de dados

res = filter(lambda x: x > media, dados) # Uma função Lambda que passa pelos iteraveis verifiando quais são os valores
# acima da média
print(list(res))

# Exemplo - 2

# Remoção de dados Faltantes

paises = ['','Brasil','Portugal','','Rússia']

print(paises)

#res = filter(None, paises)
#res = filter(lambda pais: len(pais) > 0, paises ) # Se o tamanho da string for maior do que 0, ela passa.
res = filter(lambda pais: pais != '', paises) # Se cada valor passado na lista for diferete de '', ela passa.
print(list(res))

# Exemplo 3 - Encontranto os tweets inativos em um conjunto de dados mais complexo.

# Forma - 1

usuarios = [
    {"Username":"Jooj","tweets":["Pega o The Jooj"]},
    {"Username":"Daniel","tweets":[]},
    {"Username":"Dan","tweets":["Pega o The Jooj"]},
    {"Username":"Janaina","tweets":["Pega o The Jooj"]},
    {"Username":"Laís","tweets":[]},
    {"Username":"","tweets":["Pega o The Jooj"]}
]

inativos = list(filter(lambda pos: len(pos["tweets"]) == 0, usuarios ))

print(inativos)

usuarios = [
    {"Username":"Jooj","tweets":["Pega o The Jooj"]},
    {"Username":"Daniel","tweets":[]},
    {"Username":"Dan","tweets":["Pega o The Jooj"]},
    {"Username":"Janaina","tweets":["Pega o The Jooj"]},
    {"Username":"Laís","tweets":[]},
    {"Username":"","tweets":[]}
]

# Forma 2

ativos = list(filter(lambda pos: pos["tweets"], usuarios)) # Retorna todos os usuários ativos, "tweets" != vazio
print(ativos)

# Forma 3

inativos = list(filter(lambda pos: not pos["tweets"], usuarios)) # Retorna todos os usuários inativos, "tweets" == vazio
print(inativos)

"""

# Combinando Filters e Maps
# Escrever uma frase, utilizando um nome que possua menos de 5 caracteres.

nomes = ["Laura","Ana","Daniel"]

res = list(map(lambda nome: f"O nome da(o): {nome} é muito lindo!", filter(lambda nome: len(nome) < 5, nomes)))

print(res)

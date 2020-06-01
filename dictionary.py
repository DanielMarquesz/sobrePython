"""
Dicionários

OBS: Em algumas linguagens de programação: os dicionários Python são conhecidos por mapas.

Dicionários são  coleções do tipo chave/valor.

Os Dicionários são representados por colchetes. {}.

print(type({})

# Sobre os Dicionários

 - Chave e Valor são separados por ':' - Ex : 'chave:valor'.


paises = {'br':'Brasil','eua':'Estados Unidos','py':'Python'}
print(paises)
print(type(paises))

# Acessando Elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

# Forma 2 - Acessando via Get - (Recomendada)

print(paises.get('br'))
print(paises.get('eua'))

# Encontrando e não encontrando chaves no dicionário

paises = {'br':'Brasil','eua':'Estados Unidos','py':'Python'}
pais = paises.get('br','Não Cadastrado') # Caso não ache o a chave, retorna um valor pré definido

print(f'Encontrado: {pais}')
# Podemos verificar se determinada chave se encontra em um dicionário
paises = {'br':'Brasil','eua':'Estados Unidos','py':'Python'}

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)
"""

# Podemos Utilizar qualquer tipo de dado (int, float, string, boolean), inclusive, listas, tuplas,
# dicionários como chaves de dicionários

# Coordenadas de locais
localidades = {
    (35.3895, 39.6917): 'Escritório em Tokyo',
    (37.3445, 12.0757): 'Escritório em Rio de Janeiro',
    (25.6745, 19.4565): 'Escritório em São Paulo'
}
print(localidades)
lista = []
teste = 'oi'
for i in range(2):
    lista.append(teste)
print(lista)

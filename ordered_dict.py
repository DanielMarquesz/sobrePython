'''
Módulo Collections - Ordered Dict

# Exemplo Comun

# Em um dicionário, a ordem de inserção dos elementos não é garantida.

dicionario = {'a':1,'b':2,'c':3,'d':4}

for chave, valor in dicionario.items():
    print('Chave {} e o valor {}'.format(chave, valor))


# Exemplo Ordered

from collections import OrderedDict

dicionario = OrderedDict({'a':4,'b':2,'c':3,'d':1})

for chave, valor in dicionario.items():
    print('Chave {} e o valor {}'.format(chave, valor))

'''

from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários Comuns

dict1 = {'a':1,'b':2}
dict2 = {'b':2,'a':1}

print(dict1 == dict2) # os dicionários são Iguais?

# True, Pois dicionários comuns independente da ordem verificam se as chaves possuem os valores iguais.
# A ordem nos dicionários comuns não importa(ordem das chaves e valores)

# OrderedDict

dict1 = OrderedDict({'a':1,'b':2})
dict2 = OrderedDict({'b':2,'a':1})

print(dict1 == dict2) # os dicionários são Iguais?

# False, Pois utilizando a função OrderedDict a ordem nos dicionários importa(ordem das chaves e valores)





'''
Módulo Collections - Default Dict

# Recaptulando Dicionários

dicionario = {'curso':'De python','Escola':'Pública'}

print(dicionario)
print(dicionario['curso'])

# Exemplo 1

from collections import defaultdict

dicionario = defaultdict(lambda: 0) # Simplesmente adiciona um valor padrão (nesse caso 0)
                                    # para os valores não encontrados nas chaves do dicionário)
dicionario['curso'] = 'Curso de Python 3'
print(dicionario['chave'])
print(dicionario)

'''


'''

Módulo Collections - Counter (Contador)

Collections -> High Performance Container DataTypes

Counter -> Recebe um Interável como parâmetro(lista, tupla, dicionário, conjunto, Strings) e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de
ocorrências desse elemento.

# Exemplo 1

# Realizando o Import
from collections import Counter

# Utilizamos como exemplo uma lista
lista = [1, 2, 43, 5, 6, 7, 8, 879, 81, 87, 8, 43, 43, 43]

resultado = Counter(lista)
print(type(resultado))
print(resultado)
# mostra quantos o item e quantas vezes esse se repete
# Counter({43: 4, 8: 2, 1: 1, 2: 1, 5: 1, 6: 1, 7: 1, 879: 1, 81: 1, 87: 1})

# Exemplo 2

from collections import Counter

print(Counter('Daniel da Conceição'))

'''

# Exemplo 3

from collections import Counter

texto = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will " \
        "give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the " \
        "master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but " \
        "because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. " \
        "Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because " \
        "occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, " \
        "which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right " \
        "to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences," \
        " or one who avoids a pain that produces no resultant pleasure?"

palavras = texto.split()
print(Counter(palavras))
# imprime cada palavra e quantidade de vezes que essa se repete em toda a String

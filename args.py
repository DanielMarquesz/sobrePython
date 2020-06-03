"""
# Entendendo o *args

# Exemplo

*xis: Também é um tipo de string args

Mas por convenção, utilizamos *args(decisão da comunidade Pythônica)

O que é *args?

O parâmetro *args em uma função, coloca os valores extras informados na entrade de uma função em uma tupla, lembrando que tuplas
são imutáveis.

# Exemplo 1

def multiplicacao(num1, num2, num3): # Caso mais de 3 entradas sejam fornecidas, a execução retorna error
    return num1 * num2 * num3

print(multiplicacao(1,2,3,4))

# Exemplo 2

def multiplicacao(*args): # Com *args, se torna ilimitada a quantidade de entradas
    total = 1
    for num in args: # pega todos os valores na tuplas 'args' na posicao'num' e multiplica com a variácel total
        total = total * num
    return total
print(multiplicacao(1,2,3,5)) # Com *args, se torna ilimitada a quantidade de entradas

# Exemplo 3

def varias_entradas(nome, email, *args): # Nome e Email são parâmetros obrigatórios
    return nome, email, args

print(varias_entradas('Daniel','daniel@yahoo.com','sanduíche',3.1415))

# Exemplo 4

def verifica(*args):
    if 'Lais' in args and 'Alves' in args:
        return 'Laís está aqui!'
    else:
        return 'Laís não está aqui =('

print(verifica())
print(verifica('Daniel',12,'Marques','Lais'))
print(verifica(False, 'Udom','Lais','Alves'))


# Exemplo de desempacotamento com arg

print(soma_numeros(*numeros))
"""

# Exemplo 5

def soma_numeros(*args):
    return sum(args)

numeros = [1, 45, 9, 7, 32, 2] # Quando uma lista é passada para o *args ele identifica a lista como um elemento da tupla
print(soma_numeros(*numeros)) # com o "*" conseguimos desfazer a lista e ao mesmo tempo enviávla para a função *args


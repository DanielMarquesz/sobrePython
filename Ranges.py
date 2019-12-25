'''
Ranges:

- São Utilizados para gerar sequências numéricas de forma específica.

Formas de Utilização:

# Forma 1
range(valor_de_parada)
EX:

for num in range(10):
    print(num)

# Forma 2
range(valor_inicio, valor_parada)
EX:

for num in range(1, 10):
    print(num)

# Forma 3
range(valor_inicio, valor_parada, passo)
EX:

for num in range(1, 10, 2): #Ira pular de 2 em 2 numeros
    print(num)

# Forma 4
range(valor_inicial, valor_final, decrementador)
EX:

for num in range(10, 0, -2): #diminuira de 2 em 2
    print(num)

'''
for num in range(10, 0, -2): #diminuira de 2 em 2
    print(num)

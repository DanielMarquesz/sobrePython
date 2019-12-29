'''
Saindo de Loops While utilizando o break

Utilizado para sair de loops de Maneira projetada

Ex 1:
for num in range(2, 12):
    if num == 8:
        break
    else:
        print(num)
print('Saiu do Loop')

'''
#Ex 2:

while True:
    comando = input('Digite "Sair" para sair: ').upper()
    if comando == "SAIR":
        break

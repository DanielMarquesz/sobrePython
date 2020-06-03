'''
**kwargs

Diferente do *args, o **kwargs exige que usemos parâmetros nomeados e transforma esses parâmetros extras em dicionários.
Outra diferença do *args é que o **kwargs armazena os elements excedentes em um dicionário, sendo necessário no recebimento
uma chave e valor ao parâmetro.

# Exemplo 1

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'O ser humano {pessoa} gosta da cor {cor.title()}') # A função Title Poe as letras maiúsculas

cores_favoritas(Julia = "preta", Margo='branca')

# Exemplo 2

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Vc recebeu um Cumprimento Pythônico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem vc é...'

print(cumprimento_especial())
print(cumprimento_especial(geek ='Python'))
print(cumprimento_especial(pedra ='Papel'))

# De forma geral, em funções podemos ter (Nesta exata ordem):

1° - Parâmentros Obrigatórios
2° - *args
3° - Parâmetros Padrões(Default, Não obrigatórios também)
4° - **kwargs

# Exemplo 3

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs): # Forma e ordem correta entrade parametros
    print(idade, nome)
    print(args)
    print(solteiro)
    print(kwargs)

minha_funcao(22,'Marques') # parâmetros obrigatórios
minha_funcao(34,'Diferente',1,2,5,4, Baleia=True)# args e default
minha_funcao(12,'Sonia',Solteiro=True, banana='split',sorvete='calda') # default e kwargs


# Desempacotamento com **kwargs

def desempacota(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}' # mostra o conteúdo com as chaves "nome" e "sobrenome"

nomes = {'nome':'Felicity','sobrenome':'Smoak'}

print(desempacota(**nomes))

nomes = {'nome':'Felicity','sobrenome':'Smoak'}
print(type(nomes))
print(type(nome))

'''

def soma_multiplos(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(d=1, j=2, c=3)

# o Desempacotamento *args funciona para os tipos de coleção abaixo.
soma_multiplos(*lista)
soma_multiplos(*tupla)
soma_multiplos(*conjunto)

# Agora para o desempacotamento de dicionários Utilizamos **

soma_multiplos(**dicionario) # Um detalhe, caso as chaves do dicionário não seja iguais aos parametrôs requeridos o mesmo não funciona

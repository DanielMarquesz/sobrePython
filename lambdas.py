'''
O que são Lambdas?

São funções sem nome, ou seja, funções anônimas.

# Exemplo 1

# Função Comum
def pera(a, b):
    return a + b

#Função Lambda
uva = lambda a, b: a + b

print(pera(3, 8))
print(uva(3, 8))

# Exemplo 2

nome_completo = lambda nome, sobrenome: nome.strip().title() +' '+ sobrenome.strip().title()
print(nome_completo("daniel",'   MARques'))
print(nome_completo("SILVA",'aRanTES  '))

# Exemplo 3

nomes = ['Daniel da Conceição Marques','Sonia Regina da Conceição Carola','Manoel Silva de Oliveira',
         'Laís Alves de Souza','Thaís Alves de Souza']

print(nomes)
# Função lamda que oerdena os nomes em ordem alfabética pelos sobrenomes
nomes.sort(key= lambda sobrenome: sobrenome.split(' ')[-1].lower()) # A função sort já passa em cada item de uma lista

print(nomes)

'''



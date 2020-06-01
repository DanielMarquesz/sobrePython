'''
Classes

class Paleto:

    cor = 'Pretos'
    def botao():
        return '8 botoes'

classeBotao = Paleto.botao()
classeCor = Paleto.cor
print(classeBotao, classeCor)

# Em Python , por convenção, ficou estabelecido que todo atributo de uma classe deve ser declarado como público
Ou seja, pode ser Utilizado em todo o Projeto.
Caso queiramos estabelecer um atributo como privado basta colocarmos "__" na frente de seu nome.

class Lampada:

    def __init__(self, voltagem, cor, marca, ligada):
        self.voltagem = voltagem
        self.cor = cor
        self.marca = marca
        self.ligada = ligada

# Chamando a Classe "Lampada" e adicionando os atributos

oleo = Lampada(110, 'amarela',  'light', True)
print(oleo.cor)


user = Acesso('daniel@gmail.com','2345678')

print(user.email)               # Acessando um Atributo Público
print(user._Acesso__senha)      # Acessando um atributo privado (Forma Incorreta de se ACessar um Atributo Protegido).
user.mostra_senha()             # Acessa um atributo privado dentro de sua própria classe através de um método dela mesma.

# O que São Atributos de Instância?

# Quando criamos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.
daniel = Acesso('emaildaniel@gmail.com','1234')
sonia = Acesso('emailsonia@gmail.com','4321')

daniel.mostra_email()
daniel.mostra_senha()
print()
sonia.mostra_email()
sonia.mostra_senha()

# Atributos de Classe

class Produto:

    imposto = 1.05 # Esse é um Atributo de Classe
    contador = 0 # Contador para verificar quantas vezes o objeto foi instânciado

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1 # Atributo de instância 'id' recebe + 1
        self.nome = nome # Esse é um Atributo de Instância/ que fica dentro do método
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id # O Atributo de classe contador recebe o valor de 'id'

p1 = Produto("Chinelo", "de dedo", 10)
p2 = Produto("Xbox", "Microsoft", 250)

print(p2.valor) # Multiplica o valor do produto pelo valor do imposto
print(p1.valor) # Multiplica o valor do produto pelo valor do imposto

# Como imposto não é um atributo de instância(não esta dentro de um método), podemos acessa-lo diretamente pela classe

# Cada objeto já instânciado pela classe produto reberá um ID, referente a quantidade de chamadas já realizadas ali
print(p1.id)
print(p2.id)

print(Produto.imposto)


'''

# Classes com Atríbutos Públicos
class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    # Os atributos dentro dos Métodos são chamados de atributos de Instância
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.senha = senha
        self.email = email

# Atributos Públicos e Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email  # Atributo Público
        self.__senha = senha  # Atributo Privado

    def mostra_senha(self): # Método que mostra a senha que estava em modo privado dentro da própria classe.
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# Atributos Dinâmicos -> Atributos de Instância que podem ser criados em tempo de execução.
# Obs:
class Produto:

    imposto = 1.05 # Esse é um Atributo de Classe
    contador = 0 # Contador para verificar quantas vezes o objeto foi instânciado

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1 # Atributo de instância 'id' recebe + 1
        self.nome = nome # Esse é um Atributo de Instância/ que fica dentro do método
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id # O Atributo de classe contador recebe o valor de 'id'

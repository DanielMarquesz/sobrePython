'''
POO - Métodos

- Métodos (funções) => Representam o comportamento do objeto. Ou seja, as ações que este objeto
pode realizar no seu sistema.

Em Python, dividimos métodos em 2 grupos : Métodos de Instância e métodos de Classe

# Métodos de Instância

# O método dunder init __init__ é um método especial chamdo de construtor e sua função é construir o objeto apartir da classe.
# Não é de maneira nenhum recomendado utilizar o método __dunder__ em nenhum classe criada no python

OBS: Todo elemento que inicia e finaliza com UnderLine em Python é chamado de dunder

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

prod = Produto('Pc Gaymer', 'Eletrônico',1500.00)
print(prod.desconto(10))

# Métodos de Instância
user1 = Usuario('Angelina','Joulie','angelina@joulie.com','mesocorre')
user2 = Usuario('Fred','Kayo','perereca@ra.com','socorreme')

print(user1.nome_completo()) # Imprimindo nome e sobre nome
print(user2.nome_completo()) # Imprimindo nome e sobre nome

print(f'Senha User 1: {user1._Usuario__senha}') # Acesso de forma incorreta a um atributo de classe privado
print(f'Senha User 2: {user2._Usuario__senha}') # Acesso de forma incorreta a um atributo de classe privado


nome = input('Informe o Nome: ')
sobrenome = input('Informe o Sobrenome: ')
email = input('Informe o Email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme sua Senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('As senhas não Conferem! ')
    exit(404)

print('Usuário criado com Sucesso!')

senha = input('Informe a senha para acesso!: ')

if user.checa_senha(senha):
    print('Acesso permitido!')
else:
    print('Acesso Negado!')

print(f'Senha do Usuário Criptografada: {user._Usuario__senha}')# Forma Incorreta

# Métodos de Classe, são conhecidos como métodos estáticos em outras linguagens

# Criamos Métodos de Instância,(checa_senha) quando esses métodos precisam acessar atributos, quando não necessário
# são criados métodos de classe (conta_usuarios)

# Métodos de Classe

user = Usuario('Daniel', 'Marques','daniel@daniel.com','123456') # Adcionando um usuário
user1 = Usuario('Daniel', 'Marques','daniel@daniel.com','123456') # Adcionando um usuário
Usuario.conta_usuarios() # Forma Correta
user.conta_usuarios() # Forma corrreta, mas não recomendada
'''

from passlib.hash import pbkdf2_sha256 as cryp
import os

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 2020# NúmeroCC: Isso serve para gerar um número de conta corrente
    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1 # NúmeroCC: Isso serve para gerar um número de conta corrente
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero# NúmeroCC: Isso serve para gerar um número de conta corrente

#daniel = ContaCorrente(200, 1500)
#print(daniel.numero)

class Produto:

    contador = 0 # NúmeroProdutos: Isso serve para gerar a quantidade de produtos

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador +1 # NúmeroProdutos: Isso serve para gerar a quantidade de produtos
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id # NúmeroProdutos: Isso serve para gerar a quantidade de produtos

    def desconto(self, porcentagem):
        '''Retorna o Valor do produto com Desconto'''
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod # Decorador
    def conta_usuarios(cls): # Um contador para saber quantos usuários criados existem
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha): # Método de classe
        self.__id = Usuario.contador +1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 200000, salt_size = 16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self): # Método para retornar o primeiro nome e o sobrenome
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self): # Assim como um atributo, um método tb pode ser privado utilizando se duplas "_"
        return self.__email.split('@')[0]

Usuario.ver()
Usuario.conta_usuarios()
user = Usuario('Daniel', 'Marques', 'pereira@gmail.com','321654')
Usuario.conta_usuarios()

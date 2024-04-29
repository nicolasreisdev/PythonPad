
class Banco(object): # Classe mãe , ou superclasse, herda de object (classe base do Python) // boa prática
    def __init__(self, saldo, ID): # Método construtor
        self.__ID = ID # Atributo da classe (privado), ao colocar __ na frente do atributo, ele se torna privado
        self.saldo = saldo # Atributo da classe
        
class Conta(Banco): # Classe filha
    """
    Classe que representa uma conta bancária
    """
    __total = 20000 # Atributo estático (privado)
    reserva = 0.1 # Atributo estático
    def __init__(self, nome, saldo, ID): # Método construtor
        super(Conta, self).__init__(saldo, ID) # Chamando o construtor da classe mãe
        Banco.__init__(self,saldo, ID) # Chamando o construtor da classe mãe
        self.nome = nome # Atributo exclusivo da classe Conta
    def deposito(self, valor): # Método comum a todas as classes filhas
        """
    Método que realiza um depósito na conta
        """
        self.saldo += valor # Acessando um atributo da classe
        Conta.__total += valor
    def saque(self, valor): # Método comum a todas as classes filhas
        """
    Método que realiza um saque na conta
        """
        self.saldo -= valor # Acessando um atributo da classe
        Conta.__total -= valor
    def imprime(): # Método estático
        print("Saldo: ", Conta.__total) # Acessando um atributo da classe
    def imprimeReserva(): # Método estático
        print("Reserva: ", Conta.reserva*Conta.__total) # Acessando um atributo da classe
        
itau = Conta("Nicolas", 1000, 1) # Instanciando um objeto da classe Conta
itau.deposito(100) # Chamando um método da classe filha
itau.saque(50) # Chamando um método da classe filha
print(itau.saldo) # Acessando um atributo da classe
Conta.imprime() # Chamando um método estático
Conta.imprimeReserva() # Chamando um método estático
print(itau.__doc__) # Retorna a documentação da classe
print(itau.saque.__doc__) # Retorna a documentação do método
print(itau.deposito.__doc__) # Retorna a documentação do método


# Métodos estaticos são métodos que não precisam de uma instância da classe para serem chamados, ou seja, não precisam de um objeto para serem chamados
# Métodos de classe são métodos que precisam de uma instância da classe para serem chamados, ou seja, precisam de um objeto para serem chamados
# Métodos comuns são métodos que podem ser chamados por qualquer instância da classe, ou seja, podem ser chamados por qualquer objeto
# Atributos estáticos são atributos que são compartilhados por todas as instâncias da classe, ou seja, são compartilhados por todos os objetos
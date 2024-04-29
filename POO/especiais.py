
class Conta(object):
    """
    Classe que representa uma conta bancária
    """
    def __init__(self, saldo, ID): # Método construtor
        self.__ID = ID
        self.saldo = saldo 
    def __str__(self): # Método mágico que retorna uma string
        return "ID: "+str(self.__ID)+"\nSaldo: "+str(self.saldo)
    def __add__(self, other): # Método mágico que sobrecarrega o operador +
        self.saldo += other.saldo
        return self
    def __sub__(self, other): # Método mágico que sobrecarrega o operador -
        self.saldo -= other.saldo
        return self
    def __mul__(self, other): # Método mágico que sobrecarrega o operador *
        self.saldo *= other.saldo
        return self
    def __div__(self, other): # Método mágico que sobrecarrega o operador /
        self.saldo /= other.saldo
    def __truediv__(self, other): # Método mágico que sobrecarrega o operador /
        self.saldo /= other.saldo
        return self
    def __eq__(self, other): # Método mágico que sobrecarrega o operador ==
        return self.saldo == other.saldo
    def __ne__(self, other): # Método mágico que sobrecarrega o operador !=
        return self.saldo != other.saldo
    def __lt__(self, other): # Método mágico que sobrecarrega o operador <
        return self.saldo < other.saldo
    def __gt__(self, other): # Método mágico que sobrecarrega o operador >
        return self.saldo > other.saldo
    def __le__(self, other): # Método mágico que sobrecarrega o operador <=
        return self.saldo <= other.saldo
    def __ge__(self, other): # Método mágico que sobrecarrega o operador >=
        return self.saldo >= other.saldo
    def __len__(self): # Método mágico que retorna o tamanho do objeto
        return len(str(self.saldo))
    def __getitem__(self, key): # Método mágico que retorna um item do objeto
        return str(self.saldo)[key]
    
itau = Conta(1000, 1) # Instanciando um objeto da classe Conta
print(itau.__doc__) # Retorna a documentação da classe


class Conta(object):
    """
    Classe que representa uma conta bancária
    """
    def __init__(self, saldo, ID, nome): # Método construtor
        self.nome = nome
        self.ID = ID # Para que o método sort funcione, é necessário que o atributo seja público
        self.saldo = saldo 
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




class Contas(list): # Herdando de list
    def sort (self): # Método que sobrescreve o método sort da classe list
        copia = self.copy() # Copiando a lista
        tam = len(self) # Tamanho da lista
        self.clear() # Limpando a lista
        while len(self) < tam: # Enquanto a lista não estiver ordenada
            min_id = copia[0] # Menor ID    
            for conta in copia: # Percorrendo a lista
                if conta.ID < min_id.ID: # Se o ID da conta for menor que o menor ID
                    min_id = conta # Atribui a conta ao menor ID
            self.append(min_id) # Adiciona o menor ID a lista
            copia.remove(min_id) # Remove o menor ID da lista copia
            



class Banco: # Classe que representa um banco
    def __init__(self): # Método construtor
        self.contas = Contas() # Lista de contas (para que o método sort funcione, é necessário que o atributo seja público)
        
itau = Conta(1000, 3, "Itau") # Instanciando um objeto da classe Conta
bradesco = Conta(500, 1, "Bradesco") # Instanciando um objeto da classe Conta
satander = Conta(1500, 2, "Satander") # Instanciando um objeto da classe Conta
banco = Banco() # Instanciando um objeto da classe Banco
banco.contas.append(itau) # Adicionando a conta itau a lista de contas do banco
banco.contas.append(bradesco) # Adicionando a conta bradesco a lista de contas do banco
banco.contas.append(satander) # Adicionando a conta satander a lista de contas do banco
banco.contas.sort() # Ordenando as contas do banco

for conta in banco.contas: # Percorrendo a lista de contas do banco
    print(conta.__dict__) # Imprimindo o dicionário da conta
    print() # Quebrando a linha
        
        

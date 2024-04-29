
class Automovel(object): # Classe mãe , ou superclasse, herda de object (classe base do Python) // boa prática
    def __init__(self, marca, modelo, ano, cor): # Método construtor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def acelerar(self): # Método comum a todas as classes filhas
        print('Acelerando...')

    def frear(self): # Método comum a todas as classes filhas
        print('Freando...')
    def som(self): # Método comum a todas as classes filhas
        pass # Método abstrato que será sobrescrito nas classes filhas (polimorfismo)
        
class Carro(Automovel): # Classe filha
    def __init__(self, marca, modelo, ano, cor, portas): # Método construtor
        super(Carro, self).__init__(marca, modelo, ano, cor) # Chamando o construtor da classe mãe
        Automovel.__init__(self, marca, modelo, ano, cor) # Chamando o construtor da classe mãe
        #ambos os métodos acima são equivalentes
        self.portas = portas

    def abrir_portas(self): # Método exclusivo da classe Carro
        print('Abrindo portas...')
        
    def fechar_portas(self): # Método exclusivo da classe Carro
        print('Fechando portas...')
    def som(self): # Método comum a todas as classes filhas
        print('Som do carro...') # Método abstrato da classe mãe sobrescrito na classe filha (polimorfismo)
        
class Moto(Automovel): # Classe filha
    def __init__(self, marca, modelo, ano, cor, cilindradas): # Método construtor
        super(Moto, self).__init__(marca, modelo, ano, cor) # Chamando o construtor da classe mãe
        Automovel.__init__(self, marca, modelo, ano, cor) # Chamando o construtor da classe mãe
        #ambos os métodos acima são equivalentes
        self.cilindradas = cilindradas

    def empinar(self): # Método exclusivo da classe Moto
        print('Empinando...')
        
    def derrapar(self): # Método exclusivo da classe Moto
        print('Derrapando...')
    def som(self): # Método comum a todas as classes filhas
        print('Som da moto...') # Método abstrato da classe mãe sobrescrito na classe filha (polimorfismo)
        

carro = Carro('Mitsubishi', 'Pajero', 2024, 'Prata', 4) # Instanciando um objeto da classe Carro
carro.som() # Chamando um método da classe filha
print("Agora é a vez da moto..")
moto = Moto('Honda', 'CBR', 2024, 'Vermelha', 1000) # Instanciando um objeto da classe Moto
moto.som() # Chamando um método da classe filha

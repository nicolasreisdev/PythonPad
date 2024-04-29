
class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def engordar(self, peso):
        self.peso += peso
    def emagrecer(self, peso):
        self.peso -= peso
    def crescer(self, altura):
        self.altura += altura 
    def envelhecer(self, anos):
        if(self.idade < 21):
            for i in range(anos):
                if(self.idade > 21):
                    self.idade += anos-i
                    break
                self.idade+=1
                self.crescer(0.05)
        else: self.idade += anos    
    def imprime(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Peso: ", self.peso)
        print("Altura: ", self.altura)
    
pessoa = Pessoa("Nicolas", 16, 70, 1.60)
pessoa.imprime()
pessoa.envelhecer(7)
print("\nEnvelhecendo 7 anos")
pessoa.imprime()


class Pessoa:
    def __init__(self, nome, idade, emprego):
        self.nome = nome
        self.idade = idade
        self.emprego = emprego
    def dados(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Emprego: ", self.emprego)
        
nicolas = Pessoa("Nicolas", 16, "Estudante") # Create an object with parameters
print(nicolas.__dict__) # returns a dictionary with the attributes of the object
print(nicolas.__doc__) # returns the class documentation
print(nicolas.__module__) # returns the module where the class is defined
print(nicolas.__class__) # returns the class of the object
print(nicolas.__class__.__name__) # returns the name of the class of the object
nicolas.dados() # Call the method
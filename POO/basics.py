

class my_object():
    def __init__(self): # Constructor without parameters
        self.name = "my_object"
        self.value = 0
        print("Object created")
    def imprime(self): # Method
        print("Name: ", self.name)
        print("Value: ", self.value)

class my_object_parameters():
    def __init__(self, name, value=0): # Constructor with parameters , value has a default value 0 (optional parameter)
        self.name = name
        self.value = value
        print("Object created")
    def imprime(self): # Method
        print("Name: ", self.name)
        print("Value: ", self.value)
        
print("Object 1, without parameters")
obj = my_object() # Create an object empty
obj.imprime()
print("\nObject 2 with parameters")
nic = my_object_parameters("Nicolas", 10) # Create an object with parameters
nic.imprime()
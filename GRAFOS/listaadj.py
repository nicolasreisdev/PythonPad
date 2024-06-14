"""
Implementação de um grafo com lista de adjacência
Implementação: Nicolas Reis - 14/06/2024
"""



class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)] # Lista de adjacência, inicializada com listas vazias
                            # for i in range(self.vertices) percorre a lista e cria uma lista para cada vértice
                            
    def add_aresta_simple(self, u, v):
        self.grafo[u-1].append(v)
        #self.grafo[v-1].append(u) #grafo não direcionado
        
    
    def add_aresta_peso(self, u, v, peso):
        self.grafo[u-1].append([v, peso])
        #self.grafo[v-1].append([u, peso]) #grafo não direcionado
    
    def show(self):
        for i in range(self.vertices):
            print(f"{i+1}:" , end=" ")
            for j in self.grafo[i]:
                print(j, end=" ") 
            print()  
            
            
            
v = int(input("Digite o número de vértices: "))
g = Grafo(v)
a = int(input("Digite o número de arestas: "))
for i in range(a):
    u, v, peso = map(int, input("Digite os vértices da aresta: ").split())
    g.add_aresta_peso(u, v, peso)
    
g.show()
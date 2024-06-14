"""
Implementação de um grafo com matriz de adjacência
Implementação: Nicolas Reis - 14/06/2024
"""

class Grafo: 
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] # Matriz de adjacência, inicializada com zeros
                                                        # ([0]*self.vertices) cria uma lista com a quantidade de vertices iguais a zero
                                                        # for i in range(self.vertices) percorre a lista e cria uma lista para cada vértice
        
    def add_aresta_simple(self, u, v):
        self.grafo[u-1][v-1] = 1 # Adiciona uma aresta entre os vértices u e v (u-1 e v-1 pois a matriz começa em 0), trocar = por += para grafos múltiplos
        #self.grafo[v-1][u-1] = 1 #grafo não direcionado
        
    def add_aresta_peso(self, u, v, peso):
        self.grafo[u-1][v-1] = peso # Adiciona uma aresta entre os vértices u e v com peso
        #self.grafo[v-1][u-1] = peso #grafo não direcionado    

    def show(self):
        for i in range(self.vertices):
            print(self.grafo[i])
            
            
            
v = int(input("Digite o número de vértices: "))
g = Grafo(v)
a = int(input("Digite o número de arestas: "))
for i in range(a):
    u, v, peso = map(int, input("Digite os vértices da aresta: ").split())
    g.add_aresta_simple(u, v, peso)
    
            
               
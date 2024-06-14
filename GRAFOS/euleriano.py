"""
Implementação de um grafo simples e direcionado com matriz de adjacência
- add_aresta_simple(u, v): Adiciona uma aresta entre os vértices u e v
- add_aresta_peso(u, v, peso): Adiciona uma aresta entre os vértices u e v com peso
- show(): Mostra a matriz de adjacência
- tem_aresta(u, v): Verifica se existe aresta entre u e v
- euleriano(): Verifica se o grafo é euleriano, semi-euleriano ou não euleriano

Para um grafo ser euleriano, segue as seguintes regras:
- Todos os vértices têm grau par
- O grafo é conexo
- Se o grafo não é conexo, cada componente conexo deve ser euleriano
    
Para um grafo ser semi-euleriano, segue as seguintes regras:
- Existe exatamente dois vértices de grau ímpar
- um vértice de grau ímpar é o início do caminho euleriano e o outro é o fim
- O grafo é conexo
- Se o grafo não é conexo, cada componente conexo deve ser semi-euleriano

*Caso o grafo tenha mais que dois vértices de grau ímpar, ele não é euleriano nem semi-euleriano.

Implementação: Nicolas Reis - 14/06/2024
"""



class Grafo: 
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] # Matriz de adjacência, inicializada com zeros
                                                        # ([0]*self.vertices) cria uma lista com a quantidade de vertices iguais a zero
                                                        # for i in range(self.vertices) percorre a lista e cria uma lista para cada vértice
        
    def add_aresta_simple(self, u, v):
        self.grafo[u-1][v-1] += 1 # Adiciona uma aresta entre os vértices u e v (u-1 e v-1 pois a matriz começa em 0), trocar = por += para grafos múltiplos
        if u != v:
            self.grafo[v-1][u-1] += 1 #grafo não direcionado
        
    def add_aresta_peso(self, u, v, peso):
        self.grafo[u-1][v-1] = peso # Adiciona uma aresta entre os vértices u e v com peso
        #self.grafo[v-1][u-1] = peso #grafo não direcionado    

    def show(self):
        for i in range(self.vertices):
            print(self.grafo[i])
            
    def tem_aresta(self, u, v):
        if self.grafos[u-1][v-1] != 0:
            print(f'Existem {self.grafos[u-1][v-1]} arestas entre {u} e {v}')
        else:
            print(f'Não existem arestas entre {u} e {v}')
        
    def euleriano(self):
        cont  = 0
        for i in range(self.vertices): # Percorre as linhas
            grau = 0
            for j in range(self.vertices): # Percorre a linha i
                if i == j:
                    grau = grau + 2*self.grafo[i][j] # Se for laço
                else:
                    grau += self.grafo[i][j] # Soma o grau de saída
            if grau % 2 != 0: # Se o grau for ímpar
                cont += 1
        
        if cont == 0:
            print("O grafo é euleriano")
        elif cont == 2:
            print("O grafo é semi-euleriano")
        else:
            print("O grafo não é euleriano")
            
            
            
v = int(input("Digite o número de vértices: "))
g = Grafo(v)
a = int(input("Digite o número de arestas: "))
for i in range(a):
    u, v= map(int, input("Digite os vértices da aresta: ").split())
    g.add_aresta_simple(u, v)
    
g.euleriano()
g.show()
    
            
               
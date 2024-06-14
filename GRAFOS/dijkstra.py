"""
Implementação do algoritmo de Dijkstra para encontrar o menor caminho entre dois vértices de um grafo ponderado.
Implementação com heap min (fila de prioridade mínima) e sem heap.
Implementação: Nicolas Reis - 14/06/2024
"""

import math

class HeapMin: # Heap min (Fila de prioridade minima)
    def __init__(self):
        self.heap = []
        self.node = 0
    
    def add_element(self, element, weight):
        self.heap.append([element, weight])
        self.node += 1
        filho = self.node
        while True:
            if filho == 1:
                break
            pai = filho//2 
            if self.heap[pai-1][1] <= self.heap[filho-1][1]: 
                break
            else:
                self.heap[pai-1], self.heap[filho-1] = self.heap[filho-1], self.heap[pai-1]
                filho = pai
                
    def remove_element(self):
        root = self.heap[0]
        
        self.heap[0] = self.heap[self.node-1]
        self.heap.pop()
        self.node -= 1 
        pai = 1 
        while True:
            filho = pai*2 
            if filho > self.node:
                break
            if filho+1 <= self.node and self.heap[filho-1][1] < self.heap[filho][1]:
                filho += 1
            if self.heap[pai-1][1] >= self.heap[filho-1][1]:
                break
            else: 
                self.heap[pai-1], self.heap[filho-1] = self.heap[filho-1], self.heap[pai-1] 
                pai = filho 
        
        return root 
    
    def empty(self):
        if self.node == 0:
            return True
        return False
    
class GraphwithHeap: # Dijsktra com heap
    def __init__(self, vert):
        self.vert = vert
        self.graph = [[] for i in range(self.vert)]
    
    def build(self, u, v, w):
        self.graph[u-1].append([v, w])
        self.graph[v-1].append([u, w])
        
    def dijkstra(self, x):
        priority_queue = HeapMin()
        dist = [[float('inf')]*self.vert]
        dist[x-1] = 0 
        visited = [[False] for i in range(self.vert)]
        
        priority_queue.add_element(x,0)
        
        while not priority_queue.empty():
            current, weight = priority_queue.remove_element()
            if not visited[current-1]:
                continue
            visited[current-1] = True
            
            for i in self.graph[current-1]:
                distance = i[1] 
                neighbor = i[0] 
                if (dist[current] + distance) < dist[neighbor]: 
                    dist[neighbor] = dist[current] + distance 
                    priority_queue.add_element(neighbor, dist[neighbor])
                    
                    
        return dist

class GraphwithoutHeap: # Dijsktra sem heap
    def __init__(self, vert):
        self.vert = vert
        self.graph = [[] for i in range(self.vert)]
        
    def add_edge(self, u, v, w):
        self.graph[u-1].append([v, w])
        self.graph[v-1].append([u, w])
        
    def dijkstra(self, x):
        dist = [[float('inf')]*self.vert] # Inicializa as distâncias com infinito
        dist[x-1] = 0 # A distância do vértice inicial é 0
        visited = [[False]*self.vert] # Inicializa a lista de visitados
        
        
        while True:
            current = -1
            weight = float('inf')
            for i in range(self.vert): # Encontra o vértice com menor distância
                if not visited[i] and dist[i] < weight:
                    current = i
                    weight = dist[i]
            
            if current == -1: # Se não houver vértices para visitar
                break
            
            visited[current] = True
            
            for i in self.graph[current]: # Atualiza as distâncias dos vizinhos
                distance = self.graph[current][1] # Peso da aresta
                neighbor = i # Vértice vizinho
                if dist[current] + distance < dist[neighbor]: # Se a distância atual for menor que a distância armazenada
                    dist[neighbor] = dist[current] + distance 
                    
        return dist
    
    
    
g = GraphwithoutHeap(7)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 6)
g.add_edge(1, 4, 10)
g.add_edge(2, 5, 13)
g.add_edge(3, 4, 3)
g.add_edge(3, 5, 11)
g.add_edge(3, 6, 6)
g.add_edge(4, 5, 6)
g.add_edge(4, 6, 4)
g.add_edge(5, 7, 3)
g.add_edge(6, 7, 8)

ans = g.dijkstra(1)
print(ans)



"""
Implementação de um heap max (árvore binária) em Python.

Uma árvore binária é uma estrutura de dados que consiste em um conjunto de nós, onde cada nó tem no máximo dois filhos, um à esquerda e outro à direita.
Um heap é uma árvore binária que obedece a uma propriedade específica, onde o pai é maior que os filhos (heap max) ou menor que os filhos (heap min).
Heap pode ser utilizado para implementar filas de prioridade, algoritmos de ordenação, entre outros.

Um heap segue as seguintes regras:
- A árvore é completa, ou seja, todos os níveis estão completos, exceto o último, que é preenchido da esquerda para a direita.
- O pai é maior que os filhos (heap max) ou menor que os filhos (heap min).
- A altura da árvore é log(n), onde n é o número de elementos.
- A inserção e remoção de elementos são feitas em O(log(n)).
- O maior elemento (raiz) é o primeiro elemento da lista.
- O filho da esquerda de um nó i é 2*i e o filho da direita é 2*i+1.
- O pai de um nó i é i//2.
- O heap é armazenado em uma lista.
Implementação: Nicolas Reis - 14/06/2024
"""



class HeapMax:
    def __init__(self):
        self.heap = []
        self.node = 0
    
    def add_element(self, element):
        self.heap.append(element)
        self.node += 1
        filho = self.node # Posição do filho 
        while True:
            if filho == 1:
                break
            pai = filho//2 # Divisão inteira, para encontrar a posição do pai (arredonda para baixo) 
                # essa estrutura é utilizada para fazer a árvore binária, onde o pai é a posição do filho dividido por 2
                # e o filho é a posição do pai*2 ou pai*2+1 na lista (começando em 1)
            if self.heap[pai-1] >= self.heap[filho-1]: # Se o pai for maior que o filho # <= para heap min
                break
            else: # Se o pai for menor que o filho
                self.heap[pai-1], self.heap[filho-1] = self.heap[filho-1], self.heap[pai-1]
                filho = pai
                
    def remove_element(self):
        root = self.heap[0] # Salva a raiz
        
        self.heap[0] = self.heap.pop() # Remove a raiz e coloca o último elemento no lugar
        self.node -= 1 # Diminui o número de elementos
        pai = 1 # Posição do pai
        while True:
            filho = pai*2 # Posição do filho da esquerda
            if filho > self.node:
                break
            if filho+1 <= self.node and self.heap[filho-1] < self.heap[filho]: # Se o filho da direita for maior que o da esquerda (> para heap min)
                filho += 1
            if self.heap[pai-1] >= self.heap[filho-1]:
                break
            else: # Se o pai for menor que o filho
                self.heap[pai-1], self.heap[filho-1] = self.heap[filho-1], self.heap[pai-1] # Troca o pai com o filho
                pai = filho # O pai agora é o filho
        
        return root  # Retorna a raiz

    def size(self): # Retorna o número de elementos
        return self.node
    
    def biggest_element(self): # Retorna o maior elemento (raiz)
        if self.nos != 0:
            return self.heap[0]
        return None
    
    def son_left(self, i): # Retorna o filho da esquerda
        if self.node >= 2*i:
            return self.heap[2*i-1]
        return None
    
    def son_right(self, i): # Retorna o filho da direita
        if self.node >= 2*i+1:
            return self.heap[2*i]
        return None
    
    def father(self, i): # Retorna o pai
        if i != 1:
            return self.heap[i//2-1]
        return None        
        
    def show(self):
        print(self.heap)
        

h = HeapMax()

for i in range(9):
    element = int(input("Digite o elemento: "))
    h.add_element(element)
    
h.show()

            
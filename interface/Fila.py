#fila FIFO para ser usada no algoritmo bfs
class Fila:
    def __init__(self,raiz,lista = []):
        self.lista = lista
        self.lista.append(raiz)

    #remove o primeiro elemento da fila (lista)
    def removefila(self):
        no = self.lista[0]
        self.lista.remove(no)
        return no

    #insere no final da fila (lista)
    def inserefila(self,no):
        self.lista.append(no)

    def retornafila(self):
        return self.lista
        
    def filavazia(self):
        return len(self.lista)==0
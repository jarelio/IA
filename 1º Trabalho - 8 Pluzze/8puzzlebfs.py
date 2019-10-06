import copy
import time
import os

class No:
    #Construtor da classe No, possui cor (usar no algoritmo bfs), 
    #lista de adjacencia (nós estados), valor (estado), pai(guarda o no do qual ele veio)
    def __init__(self,value,pai,adj=[],cor='branco'):
        self.cor = cor
        self.adj = adj
        self.value = value
        self.pai = pai

    #funcao para inserir um no na lista da adjacencia
    def __inseriradj__(self,valor):
        self.adj.append(No(valor,self))

    #funcao para criar lista de adjacencia (ao visitar um estado, ela eh chamada para criar os estados filhos)
    def crialistaadj(self):
        #estado new_value vai receber o estado referente ao estado anterior movendo o 0 para esquerda
        #caso ele seja diferente do valor atual do estado (ocorra uma mudanca)
        #o mesmo pros outros casos
        new_value = self.__movesq__()
        if(new_value != self.value):
            self.__inseriradj__(new_value)

        new_value = self.__movdir__()
        if(new_value != self.value):
            self.__inseriradj__(new_value)

        new_value = self.__movcim__()
        if(new_value != self.value):
            self.__inseriradj__(new_value)

        new_value = self.__movbai__()
        if(new_value != self.value):
            self.__inseriradj__(new_value)

    #mover para direcao, primeiro encontra a peca 0 e cria um novo estado com ela na posicao movida
    def __movesq__(self):
        linha,coluna = self.__encontrarpeca0__()
        new_value = copy.deepcopy(self.value)
        if(coluna>0):
            new_value[linha][coluna-1],new_value[linha][coluna] = self.value[linha][coluna],self.value[linha][coluna-1] 
        return new_value

    def __movdir__(self):
        linha,coluna = self.__encontrarpeca0__()
        new_value = copy.deepcopy(self.value)
        if(coluna<2):
            new_value[linha][coluna+1],new_value[linha][coluna] = self.value[linha][coluna],self.value[linha][coluna+1] 
        return new_value

    def __movcim__(self):
        linha,coluna = self.__encontrarpeca0__()
        new_value = copy.deepcopy(self.value)
        if(linha>0):
            new_value[linha-1][coluna],new_value[linha][coluna] = self.value[linha][coluna],self.value[linha-1][coluna] 
        return new_value

    def __movbai__(self):
        linha,coluna = self.__encontrarpeca0__()
        new_value = copy.deepcopy(self.value)
        if(linha<2):
            new_value[linha+1][coluna],new_value[linha][coluna] = self.value[linha][coluna],self.value[linha+1][coluna] 
        return new_value
    
    #funcao para encontrar a peca 0 na matriz 3x3
    def __encontrarpeca0__(self):
        for i in range(3):
            for j in range(3):
                if (self.value[i][j] == 0):
                    linha = i
                    coluna = j
                    return linha,coluna

#fila FIFO para ser usada no algoritmo bfs
class Fila:
    def __init__(self,raiz,lista):
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

#algoritmo bfs do cormen, com a modificacao nas linhas 108 a 112
#modificacao: ao visitar um no, verificar se ele eh o estado meta, se for,
#montar a lista_solucao que eh os estados do no meta ate a raiz (percorrendo os pais)
def bfs(r,meta):
    lista_solucao = []
    r.cor = 'cinza'
    fila = Fila(r,[])
    while(not(fila.filavazia())):
        u = fila.removefila()
        if(u.value == meta):
            while(u != None):
                lista_solucao.append(u)
                u = u.pai
            return lista_solucao
        #quando um no eh visitado (retirado da fila) cria-se a lista de nos filhos dele (adjacencia / proximos estados)
        u.crialistaadj()
        for v in u.adj:
            if(v.cor == 'branco'):
                v.cor = 'cinza'
                fila.inserefila(v)
        u.cor = 'preto'
    

def main():
    #cria o no meta pra ser testado
    meta = [[1,2,3],[4,5,6],[7,8,0]]

    #cria o no raiz (inicial) passando o estado e None (valor do pai da raiz)
    no_inicial = No([[4,1,3],[7,2,5],[0,8,6]],None)

    lista_solucao = bfs(no_inicial,meta)
    
    #lista solucao eh o caminho do valor da raiz ate o valor do estado folha
    lista_solucao.reverse()
    
    #Print animado da solução
    for i in lista_solucao:
       print (i.value)

    no_inicial2 = No([[1,2,3],[4,5,6],[7,0,8]],None)
    lista_solucao2 = bfs(no_inicial2,meta)
    lista_solucao.reverse()
    
    print("--------\n")
    for i in lista_solucao2:
        print(i.value)
main()
import copy
import time
import os

class No:
    def __init__(self,value,pai,adj=[],cor='branco'):
        self.cor = cor
        self.adj = adj
        self.value = value
        self.pai = pai

    def __inseriradj__(self,valor):
        self.adj.append(No(valor,self))

    def crialistaadj(self):

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
    
    def __encontrarpeca0__(self):
        for i in range(3):
            for j in range(3):
                if (self.value[i][j] == 0):
                    linha = i
                    coluna = j
                    return linha,coluna

class Fila:
    def __init__(self,raiz,lista = []):
        self.lista = lista
        self.lista.append(raiz)

    def removefila(self):
        no = self.lista[0]
        self.lista.remove(no)
        return no

    def inserefila(self,no):
        self.lista.append(no)

    def retornafila(self):
        return self.lista
        
    def filavazia(self):
        return len(self.lista)==0

def bfs(r,meta):
    lista_solucao = []
    r.cor = 'cinza'
    fila = Fila(r)
    while(not(fila.filavazia())):
        u = fila.removefila()
        if(u.value == meta):
            while(u != None):
                lista_solucao.append(u)
                u = u.pai
            break
        u.crialistaadj()
        for v in u.adj:
            if(v.cor == 'branco'):
                v.cor = 'cinza'
                fila.inserefila(v)
        u.cor = 'preto'
    return lista_solucao

def main():

    meta = [[1,2,3],[4,5,6],[7,8,0]]
    no_inicial = No([[4,1,3],[7,2,5],[0,8,6]],None)
    lista_solucao = bfs(no_inicial,meta)
    #solucao
    lista_solucao.reverse()
    

    #Print animado da solução
    os.system("clear")
    print("Solucionar: ")
    for i in no_inicial.value:
        print(i)
    print("-------------------------------\n")
    for i in lista_solucao:
        z = 0
        if(z==3):
            print("\n\n")
        for j in i.value:
            print(j)
            z = z + 1
        time.sleep(1)    
        os.system("clear")
        print("Solucionar: ")
        for i in no_inicial.value:
            print(i)
        print("-------------------------------\n")
    for i in meta:
        print(i)


main()
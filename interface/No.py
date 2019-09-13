import copy
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
    
    def retornaValue(self):
        return self.value

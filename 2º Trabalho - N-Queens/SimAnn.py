import copy
import random
import math
import time

class SimAnn:

    def __init__(self,board,temperatura=1,iteracoes=80000):
        self.board = board
        self.temperatura = temperatura
        self.iteracoes = iteracoes
    
    def SimulatedAnnealing(self):
        solucao = []
        for i in range(1,self.iteracoes):
            print("Iteração:", i)
            h1 = self.__calculaHeuristica__(self.board)
            print("Heuristica Board Atual: ", h1)
            if(h1 == 0):
                return self.board

            #temperatura = self.temperatura / math.sqrt(i)
            temperatura = self.temperatura
            novo_board = self.__movimentarRainhaAleatorio__(self.board)
            h2 = self.__calculaHeuristica__(novo_board)
            print("Heuristica Board Novo: ", h2)
            delta = h1 - h2
            if(delta<=0):
                #self.board = copy.deepcopy(novo_board)
                self.board = novo_board
                #solucao.append(self.board)
            else:
                probabilidade = 10**(delta/temperatura)
                p = random.random()
                if(p<probabilidade):
                    #self.board = copy.deepcopy(novo_board)
                    self.board = novo_board
                    #solucao.append(self.board)


    def __calculaHeuristica__(self,board):
        #temperatura total
        h = 0
        
        #dicionario de ataques para as diagonais
        ataques = []

        #variavel auxiliar para posicoes das rainhas
        posicao = [0,0]

        #para cada rainha
        for i in range(len(board.queens)):
            queen = board.queens[i]
            
            #proximas rainhas depois da atual
            j = i+1
            while(j<len(board.queens)):

                #calcula vertical se existir outra rainha na mesma coluna da atual
                coluna = queen[1]
                if(board.queens[j][1] == coluna):
                    h = h+1
                
                #calcula horizontal se existir outra rainha na mesma linha da atual
                linha = queen[0]
                if(board.queens[j][0] == linha):
                    h = h+1

                j = j+1

            #calcula diagonal 1

                #diagonal superior esquerda
            posicao[0]=queen[0]-1
            posicao[1]=queen[1]-1
            while(posicao[0]>=0 and posicao[1]>=0):
                if(board.board[posicao[0]][posicao[1]]=='Q' and posicao not in ataques):
                    h = h+1
                posicao[0] = posicao[0]-1
                posicao[1] = posicao[1]-1
                
                #diagonal inferior direita
            posicao[0]=queen[0]+1
            posicao[1]=queen[1]+1
            while(posicao[0]<board.n_queens and posicao[1]<board.n_queens):
                if(board.board[posicao[0]][posicao[1]]=='Q' and posicao not in ataques):
                    h = h+1
                posicao[0] = posicao[0]+1
                posicao[1] = posicao[1]+1  

            #calcula diagonal 2

                #diagonal inferior esquerda
            posicao[0]=queen[0]+1
            posicao[1]=queen[1]-1
            while(posicao[0]<board.n_queens and posicao[1]>=0):
                if(board.board[posicao[0]][posicao[1]]=='Q' and posicao not in ataques):
                    h = h+1
                posicao[0] = posicao[0]+1
                posicao[1] = posicao[1]-1

                #diagonal superior direita
            posicao[0]=queen[0]-1
            posicao[1]=queen[1]+1
            while(posicao[0]>=0 and posicao[1]<board.n_queens):
                if(board.board[posicao[0]][posicao[1]]=='Q' and posicao not in ataques):
                    h = h+1
                posicao[0] = posicao[0]-1
                posicao[1] = posicao[1]+1

            #adiciona rainhas já percorridas para não calcular ataques duplicados
            ataques.append(queen)

        return h
    
    def __movimentarRainhaAleatorio__(self,board):
        queen = random.choice(board.queens)
        posicao = random.choice(board.lista_posicoes)

        board.queens.remove(queen)
        board.queens.append(posicao)

        board.lista_posicoes.append(queen)
        board.lista_posicoes.remove(posicao)

        board.board[queen[0]][queen[1]] = '-'
        board.board[posicao[0]][posicao[1]] = 'Q'

        return board
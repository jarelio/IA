import random

class Board:
    def __init__(self,n_queens):
        self.n_queens = n_queens #numero de rainhas
        self.queens = [] #salva posicoes das rainhas
        self.lista_posicoes = self.__geraPosicoes__() #posicoes para serem usadas para escolha de rainhas
        self.board = self.__geraBoard__() #board montado
        

    def __geraBoard__(self):
        board = []
        
        #Cria board com "-" em todas as posicoes
        for i in range(self.n_queens):
            board.append( ["-"] * self.n_queens )

        #Escolhe as posicoes das rainhas e coloca elas no tabuleiro (inserindo Q na posicao)
        for i in range(0,self.n_queens):
            posicao = random.choice(self.lista_posicoes)
            self.queens.append(posicao)
            self.lista_posicoes.remove(posicao)
            board[posicao[0]][posicao[1]] = 'Q'
        
        '''
        board[1][1] = 'Q'
        board[2][2] = 'Q'
        board[1][3] = 'Q'
        board[2][0] = 'Q'
        self.queens.append([1,1])
        self.queens.append([2,2])
        self.queens.append([1,3])
        self.queens.append([2,0])
        '''
        return board

    def __geraPosicoes__(self):
        lista_posicoes = []
        #Cria posicoes para as rainhas escolherem
        for i in range(0,self.n_queens):
            for j in range(0,self.n_queens):
                lista_posicoes.append([i,j])
        return lista_posicoes
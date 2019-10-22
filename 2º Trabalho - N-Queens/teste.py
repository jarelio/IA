import copy

class SimAnn:

    def __init__(self,board):
        self.board = board
    
    def execute(self):
        h = self.__calculaHeuristica__(self.board)
        print(h)

    def __calculaHeuristica__(self,board):
        #temperatura total
        h = 0
        
        #lista de ataques para as diagonais
        ataques = []

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
                    ataques.append(posicao)
                posicao[0] = posicao[0]-1
                posicao[1] = posicao[1]-1
                
                #diagonal inferior direita
            posicao[0]=queen[0]+1
            posicao[1]=queen[1]+1
            while(posicao[0]<board.n_queens and posicao[1]<board.n_queens):
                z = j
                while(z<len(board.queens)):
                    if(board.queens[z][0]==posicao[0] and board.queens[z][1]==posicao[1]):
                        print('id ataque: ', board.queens[z],' peca: ',posicao)                        
                        h = h+1
                    z = z + 1
                posicao = [posicao[0]+1,posicao[1]+1]     

            #calcula diagonal 2

                #diagonal inferior esquerda
            posicao[0]=queen[0]+1
            posicao[1]=queen[1]-1
            while(posicao[0]<board.n_queens and posicao[1]>=0):
                z = j
                while(z<len(board.queens)):
                    if(board.queens[z][0]==posicao[0] and board.queens[z][1]==posicao[1]):
                        print('ie ataque: ', board.queens[z],' peca: ',posicao)                            
                        h = h+1
                    z = z + 1
                posicao = [posicao[0]+1,posicao[1]-1]

                #diagonal superior direita
            posicao[0]=queen[0]-1
            posicao[1]=queen[1]+1
            while(posicao[0]>=0 and posicao[1]<board.n_queens):
                z = j
                while(z<len(board.queens)):
                    if(board.queens[z][0]==posicao[0] and board.queens[z][1]==posicao[1]):
                        print('sd ataque: ', board.queens[z],' peca: ',posicao)                            
                        h = h+1
                    z = z + 1
                posicao = [posicao[0]-1,posicao[1]+1]


        return h
                
from Board import Board
from SimAnn import SimAnn
import time
import os

def main():
    n = 6
    board = Board(n)    

    simann = SimAnn(board)
    board_list = simann.SimulatedAnnealing()
    
    print("--SOLUÇÃO--")
    if(board_list != None):
    #    for board_unique in board_list:
    #        os.system("clear")
    #        #printa matriz
        for i in range(0,n):
            for j in range(0,n):
                print(board_list.board[i][j],end=" ")
            print("") 
            #time.sleep(1)
            
    else:
        print("Não foi encontrada a solução!")

main()
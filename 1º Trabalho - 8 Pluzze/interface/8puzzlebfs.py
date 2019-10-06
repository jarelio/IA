import time
import os

if __name__ == '__main__':
    #cria o no meta pra ser testado
    meta = [[1,2,3],[4,5,6],[7,8,0]]

    #cria o no raiz (inicial) passando o estado e None (valor do pai da raiz)
    no_inicial = No([[4,1,3],[7,2,5],[0,8,6]],None)

    lista_solucao = bfs(no_inicial,meta)
    
    #lista solucao eh o caminho do valor da raiz ate o valor do estado folha
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


import random
import math
import matplotlib.pyplot
import copy

def geraTabuleiro(queens):
    tabuleiro = []

    for i in range(queens):
        tabuleiro.append( ["-"] * queens )
        tabuleiro[i][i] = 'Q'

    random.shuffle(tabuleiro)

    for i in range(queens):
        print(tabuleiro[i])

    return tabuleiro


def calculaHeuristica(tabuleiro,queens):
    h = 0
    queens = len(tabuleiro)
    soma_heuristicad1 = [0] * (queens+queens-1)
    soma_heuristicad2 = [0] * (queens+queens-1)

    #diagonal da esquerda inferior para direita superior
    for i in range (0,queens):
        for j in range(0,queens):
            if(tabuleiro[i][j]=='Q'):
                soma_heuristicad1[i+j] += 1

    #diagonal da esquerda superior para a direita inferior
    for i in range (0,queens):
        for j in range(0,queens):
            if(tabuleiro[i][j]=='Q'):
                soma_heuristicad2[(j+queens-1)-i] += 1

    #print(soma_heuristicad1)
    #print(soma_heuristicad2)

    for i in range(0,(queens+queens-1)):
        if(soma_heuristicad1[i]!=0):
            h+=(soma_heuristicad1[i]-1)
        if(soma_heuristicad2[i]!=0):
            h+=(soma_heuristicad2[i]-1)

    return h

def movimentarRainha(novo_tabuleiro,queens):
    linha1 = random.randint(0,queens-1)
    linha2 = random.randint(0,queens-1)

    rainha1 = novo_tabuleiro[linha1]
    rainha2 = novo_tabuleiro[linha2]

    novo_tabuleiro[linha1] = rainha2
    novo_tabuleiro[linha2] = rainha1

    return novo_tabuleiro

def main ():
    n = 40
    iteracoes = 120000
    temperatura = 100
    heuristicas = []

    tabuleiro = geraTabuleiro(n)
    #h1 = calculaHeuristica(tabuleiro,n)
    #print(h1)

    #tabuleiro2 = movimentarRainha(tabuleiro,n)
    #for i in range(0,n):
    #    print(tabuleiro2[i])

    
    for i in range(1,iteracoes):
        #for z in range (0, n):
         #   print(tabuleiro[0][z])

        print("Iteração:", i)
        h1 = calculaHeuristica(tabuleiro,n)
        heuristicas.append(h1)
        print("Heuristica Tabuleiro Atual: ", h1)
        if(h1 == 0):
            print("--SOLUÇÃO--")
            break
        novo_tabuleiro = copy.deepcopy(tabuleiro)
        novo_tabuleiro = movimentarRainha(novo_tabuleiro,n)
        #for z in range (0, n):
         #   print(novo_tabuleiro[0][z])
        h2 = calculaHeuristica(novo_tabuleiro,n)
        heuristicas.append(h2)
        print("Heuristica Board Novo: ", h2)

        delta = h2 - h1
        temperatura = float(temperatura / math.sqrt(i))

        if(delta<=0):
            tabuleiro = copy.deepcopy(novo_tabuleiro)
        else:
           #probabilidade = 10**(-delta)
            if (temperatura == 0):
                probabilidade = 0.000001
            else:
                probabilidade = math.exp(-delta/temperatura)
            p = random.random()
            if(p<probabilidade):
                tabuleiro = copy.deepcopy(novo_tabuleiro)
    for i in range(0,n):
        print(tabuleiro[i]) 
    
    qnt_heuristicas = []
    for i in range(0,len(heuristicas)):
        qnt_heuristicas.append(i)
    matplotlib.pyplot.plot(qnt_heuristicas, heuristicas)
    matplotlib.pyplot.ylim(0, 10)
    matplotlib.pyplot.xlim(0, len(heuristicas))
    matplotlib.pyplot.show()    

main()
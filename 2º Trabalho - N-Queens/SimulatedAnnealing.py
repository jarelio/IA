import random
import math
import matplotlib.pyplot

def geraTabuleiro(queens):
    tabuleiro = []
    posicoes_rainhas = []

    for i in range(queens):
        tabuleiro.append( ["-"] * queens )

    i = 0
    while i < queens:
        lc = geraLinhaColuna(queens)
        if(tabuleiro[lc[0]][lc[1]] != 'Q'):
            tabuleiro[lc[0]][lc[1]] = 'Q'
            posicoes_rainhas.append([lc[0],lc[1]])
            i+=1

    return [tabuleiro,posicoes_rainhas]

def geraLinhaColuna(queens):
    linha = random.randint(0,queens-1)
    coluna = random.randint(0,queens-1)
    return [linha,coluna]

def calculaHeuristica(tabuleiro):
    h = 0
    rainhas_posicoes = tabuleiro[1]

    #vertical
    soma_colunas = {}
    for rainha in rainhas_posicoes:
        soma_colunas[rainha[1]] = 0
    for rainha in rainhas_posicoes:
        soma_colunas[rainha[1]] +=1
    for value in soma_colunas.values():
        h+=value-1
    
    #horizontal
    soma_linhas = {}
    for rainha in rainhas_posicoes:
        soma_linhas[rainha[0]] = 0
    for rainha in rainhas_posicoes:
        soma_linhas[rainha[0]] +=1
    for value in soma_linhas.values():
        h+=value-1

    #diagonal1
    soma_diagonal1 = {}
    for i in range((2*len(rainhas_posicoes))-1):
        soma_diagonal1[i] = 0

    for y in range(len(rainhas_posicoes)):
        linha = 0
        coluna = y

        while(linha<len(rainhas_posicoes) and coluna>=0):
            if(tabuleiro[0][linha][coluna] == 'Q'):
                soma_diagonal1[y]+=1
            linha+=1
            coluna-=1
    
    for x in range(1,len(rainhas_posicoes)):
        linha = x
        coluna = len(rainhas_posicoes)-1
        while(linha<len(rainhas_posicoes) and coluna>=0):
            if(tabuleiro[0][linha][coluna] == 'Q'):
                soma_diagonal1[x+len(rainhas_posicoes)-1]+=1
            linha+=1
            coluna-=1

    for value in soma_diagonal1.values():
        if(value>0):
            h+=value-1

    #diagonal2
    soma_diagonal2 = {}
    for i in range((2*len(rainhas_posicoes))-1):
        soma_diagonal2[i] = 0

    for y in range(len(rainhas_posicoes)):
        linha = len(rainhas_posicoes)-1
        coluna = y

        while(linha>=0 and coluna>=0):
            if(tabuleiro[0][linha][coluna] == 'Q'):
                soma_diagonal2[y]+=1
            linha-=1
            coluna-=1
    
    for x in range(len(rainhas_posicoes)-2,-1,-1):
        linha = x
        coluna = len(rainhas_posicoes)-1
        while(linha>=0 and coluna>=0):
            if(tabuleiro[0][linha][coluna] == 'Q'):
                soma_diagonal2[(2*len(rainhas_posicoes)-2)-x]+=1
            linha-=1
            coluna-=1

    for value in soma_diagonal2.values():
        if(value>0):
            h+=value-1

    return h

def movimentarRainha(tabuleiro):
    rainhas_posicoes = tabuleiro[1]
    rainha = random.choice(rainhas_posicoes)

    #remove rainha escolhida
    tabuleiro[1].remove(rainha)
    tabuleiro[0][rainha[0]][rainha[1]] = '-'

    escolhida = 0
    while(escolhida == 0):
        posicao = geraLinhaColuna(len(rainhas_posicoes)+1)
        if(tabuleiro[0][posicao[0]][posicao[1]] != 'Q'):
            tabuleiro[0][posicao[0]][posicao[1]] = 'Q'
            #adiciona rainha nova
            tabuleiro[1].append(posicao)
            escolhida = 1

    return tabuleiro  

def movimentarRainhaLinha(tabuleiro):
    rainhas_posicoes = tabuleiro[1]
    rainha = random.choice(rainhas_posicoes)

    #remove rainha escolhida
    tabuleiro[1].remove(rainha)
    tabuleiro[0][rainha[0]][rainha[1]] = '-'
    
    escolhida = 0
    linha_escolhida = 0
    while(escolhida == 0):
        rainhas = 0
        for i in range(0, len(rainhas_posicoes)):
            if (rainhas_posicoes[i][0] == linha_escolhida):
                linha_escolhida += 1
                break
            else:
                rainhas +=1
        if(rainhas == len(rainhas_posicoes)):
            escolhida = 1
    
    coluna = random.randint(0,len(rainhas_posicoes))
    tabuleiro[0][linha_escolhida][coluna] = 'Q'
    tabuleiro[1].append([linha_escolhida,coluna])

    return tabuleiro

def main ():
    n = 6
    iteracoes = 120000
    temperatura = 100
    heuristicas = []
    tabuleiro = geraTabuleiro(n)
    for i in range(1,iteracoes):
        #for z in range (0, n):
         #   print(tabuleiro[0][z])

        print("Iteração:", i)
        h1 = calculaHeuristica(tabuleiro)
        heuristicas.append(h1)
        print("Heuristica Tabuleiro Atual: ", h1)
        if(h1 == 0):
            print("--SOLUÇÃO--")
            break

        novo_tabuleiro = movimentarRainhaLinha(tabuleiro)
        #for z in range (0, n):
         #   print(novo_tabuleiro[0][z])
        h2 = calculaHeuristica(novo_tabuleiro)
        heuristicas.append(h2)
        print("Heuristica Board Novo: ", h2)

        delta = h2 - h1
        #temperatura = float(temperatura / math.sqrt(i))
        if(temperatura == 0):
            temperatura = 100
        if(delta<=0):
            tabuleiro = novo_tabuleiro
        else:
            probabilidade = 10**(-delta)
            #probabilidade = math.exp(-delta/temperatura)
            p = random.random()
            if(p<probabilidade):
                tabuleiro = novo_tabuleiro
    for i in range(0,n):
        for j in range(0,n):
            print(tabuleiro[0][i][j],end=" ")
        print("") 
    
    qnt_heuristicas = []
    for i in range(0,len(heuristicas)):
        qnt_heuristicas.append(i)
    matplotlib.pyplot.plot(qnt_heuristicas, heuristicas)
    matplotlib.pyplot.ylim(0, 10)
    matplotlib.pyplot.xlim(0, len(heuristicas))
    matplotlib.pyplot.show()    

main()
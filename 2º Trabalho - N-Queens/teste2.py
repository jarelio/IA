import random as rdn


def temperaturaAtual(custoInicial, custoFinal):
    temperatura = 1
    return 10**((custoInicial - custoFinal)/temperatura)


def copiarTabela(tabela):
    novaTabela = []
    for x in tabela:
        a = []
        for y in x:
            a.append(y)
        novaTabela.append(a)
    return novaTabela


def copiarListas(lista):
    listaCopiada = []
    for x in lista:
        listaCopiada.append(x)
    return listaCopiada


def mostrarTabela(tabela):
    print()
    for linha in tabela:
        print(linha)
    print()


def custoColuna(tabela):
    custo = 0
    for coluna in range(0, n):
        quantidadeRainhas = 0
        for linha in range(0, n):
            if tabela[linha][coluna] == 1:
                quantidadeRainhas += 1
        custo += custoDasRainhas(quantidadeRainhas)
    return custo


def custoDiagonal(tabela):
    return custoDiagonalEsquerda(tabela) + custoDiagonalDireita(tabela)


def custoDiagonal2(tabela):
    if custoDiagonalEsquerda(tabela) != 0:
        print("diagonal E")
    if custoDiagonalDireita(tabela) != 0:
        print("diagonal D")
    return custoDiagonalEsquerda(tabela) + custoDiagonalDireita(tabela)


def custoDiagonalEsquerda(tabela):
    custo = 0
    for soma in [i for i in range(0, n*2)]:
        quantidadeRainhas = 0
        for linha in range(0, n):
            for coluna in range(0, n):
                if (linha + coluna) == soma:
                    if tabela[linha][coluna] == 1:
                        quantidadeRainhas += 1
        custo += custoDasRainhas(quantidadeRainhas)
    return custo


def custoDiagonalDireita(tabela):
    custo = 0
    for i in range(0, n):
        quantidadeRainhas = 0
        for j in range(0, n-i):
            if tabela[i+j][j] == 1:
                quantidadeRainhas += 1
        custo += custoDasRainhas(quantidadeRainhas)

    for j in range(1, n):
        quantidadeRainhas = 0
        for i in range(0, n-j):
            if tabela[i][j+i] == 1:
                quantidadeRainhas += 1
        custo += custoDasRainhas(quantidadeRainhas)
    return custo


def custoDasRainhas(quantidadeRainhas):
    custo = 0
    if quantidadeRainhas > 1:
        custo = quantidadeRainhas - 1
    return custo


def funcaoCusto(tabela):
    return custoColuna(tabela) + custoDiagonal(tabela)


def funcaoCusto2(tabela):
    if custoColuna(tabela) != 0:
        print("coluna")
    if custoDiagonal2(tabela) != 0:
        print("diagonal")
    print("custo total = %d" % (custoDiagonal(tabela)+custoColuna(tabela)))


def criarTabela():
    tabela = []
    for linha in range(1, n+1):
        linhaOrdenada = [int(i/n) for i in range(1, n+1)]
        rdn.shuffle(linhaOrdenada)
        tabela.append(linhaOrdenada)
    return tabela


def criarTabelas(quantidadeTabelas):
    listaTabelas = []
    for x in range(0, quantidadeTabelas):
        listaTabelas.append(criarTabela())
    return listaTabelas


n = 10

temperatura = 50

listaTabelas = criarTabelas(100000)
listaAuxiliar = []
Resultado = []

interacao = 0
while True:
    interacao += 1
    for indiceTabela in range(len(listaTabelas)):

        tabela = listaTabelas[indiceTabela]
        tabelaInicical = copiarTabela(tabela)
        custoInicial = funcaoCusto(tabelaInicical)

        tabelaFinal = copiarTabela(tabela)

        linhaAleatoria = rdn.randint(0, n-1)
        indiceRainha = tabelaFinal[linhaAleatoria].index(1)
        tabelaFinal[linhaAleatoria][indiceRainha] = 0
        colunaAleatoria = rdn.randint(0, n-1)
        tabelaFinal[linhaAleatoria][colunaAleatoria] = 1

        custoFinal = funcaoCusto(tabelaFinal)
        print(custoFinal, custoInicial)
        if custoFinal < custoInicial:
            listaTabelas[indiceTabela] = tabelaFinal
        elif temperaturaAtual(custoInicial, custoFinal) > rdn.random():
            listaTabelas[indiceTabela] = tabelaFinal
        else:
            listaTabelas[indiceTabela] = tabelaInicical

        if funcaoCusto(listaTabelas[indiceTabela]) == 0:
            Resultado = listaTabelas[indiceTabela]
            break

    if Resultado != []:
        break


funcaoCusto(Resultado)
mostrarTabela(Resultado)
print(interacao)

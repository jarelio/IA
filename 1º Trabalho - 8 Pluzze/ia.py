import timeit
import random
import copy

META = [[1,2,3],[4,5,6],[7,8,0]]
#resolucao
class Noh:
	def __init__(self,estado,nopai,g,h):
		self.estado = estado
		self.pai = nopai
		self.g = g
		self.h = h
		#cada no guarda endereco no pai, assim da pra chegar no no inicial

	def __noigualoutro__(self,outro):
		return self.estado == outro.estado

	def __valordono__(self):
		return str(self.estado)

	def __retornaestadono__(self):
		return self.estado

def solucionavel (lista):
#Conta o numero de inversoes para ver se e solucionaval, se tiver numero de inversoo impar nao e solucionavel
#peo fato do incial ser par  
	inversoes = 0
	for i,e in enumerate(lista):
		if e == 0:
			continue
		for j in range(i+1, len(lista)):
			if lista[j]==0:
				continue
			if e > lista[j]:
				inversoes+=1
		if inversoes%2 == 1:
			return False
		else:
			return True

#Gera um estado inicial diferente de META

def geraInicial(st=META[:]):
	lista = [j for i in st for j in i]
	while True:
		random.shuffle(lista)
		st = [lista[:3]]+[lista[3:6]]+[lista[6:]]
		if solucionavel(lista) and st!= META: return st
	return 0

#achar elemento no tabuleiro, por padrao acha o vazio primeiro
def acharlugardepeca(estado,elemento=0):
	for i in range(3):
		for j in range(3):
			if estado[i][j]==elemento:
				linha = i 
				coluna = j
				return linha,coluna

#achar distancia quarteirao ??? de um estado/peca para outro fazendo a soma da euristica
def distanciaQuarteirao(st1,st2):
	dist = 0
	fora = 0
	for i in range(3):
		for j in range(3):
			if st1[i][j]==0: continue
			i2,j2 = acharlugardepeca(st2,st1[i][j])
			if i2 != i or j2 != j: fora += 1
			dist += abs(i2+1)+abs(j2+j)
		return dist + fora

#cria no g = distancia percorrida + estado atual e a meta
def criano(estado,pai,g=0):
	h = g + distanciaQuarteirao(estado,META) #heuristica A*
	teste = Noh(estado,pai,g,h)
	return teste

#inserir no na fronteira e ordena pelo menor curto total
def inserirno(no,fronteira):
	if no is fronteira:
		return fronteira
	fronteira.append(no)
	chave = fronteira[-1]
	j = len(fronteira)-2
	while fronteira[j].h > chave.h and j>=0:
		fronteira[j+1] = fronteira[j]
		fronteira[j] = chave
		j-=1
	return fronteira

#fazer movimentos no tabuleiro, "mover o branco", se move o branco pra baixo a peca sobe


def moveAbaixo(estado):
	linha,coluna = acharlugardepeca(estado)
	if linha < 2:
		estado[linha+1][coluna],estado[linha][coluna] = estado [linha][coluna],estado[linha+1][coluna]
	return estado	

def moveAcima(estado):
	linha,coluna = acharlugardepeca(estado)
	if linha > 0:
		estado[linha-1][coluna],estado[linha][coluna] = estado [linha][coluna],estado[linha-1][coluna]
	return estado		


def moveDireita(estado):
	linha,coluna = acharlugardepeca(estado)
	if linha < 2:
		estado[linha][coluna+1],estado[linha][coluna] = estado [linha][coluna],estado[linha][coluna+1]
	return estado		


def moveEsquerda(estado):
	linha,coluna = acharlugardepeca(estado)
	if linha > 0 :
		estado[linha][coluna-1],estado[linha][coluna] = estado [linha][coluna],estado[linha][coluna-1]
	return estado	

#retornar todos os sucessores do eum no, estados alcansaveis 

def sucessorno(no):
	estado = no.estado
	pai = no.pai
	if pai:
		estado = pai.estado
	else:
		estado = None

	listaS = []
	l1 = moveAcima(copy.deepcopy(estado))
	if l1 != estado:
		listaS.append(l1)

	l2 = moveDireita(copy.deepcopy(estado))
	if l2 != estado:
		listaS.append(l2)

	l3 = moveAbaixo(copy.deepcopy(estado))
	if l3 != estado:
		listaS.append(l3)

	l4 = moveEsquerda(copy.deepcopy(estado))
	if l4 != estado:
		listaS.append(l4)

	return listaS


#implementar busca A*
def buscaA(max,noInicio):
	print(noInicio, ":")
	numerodemov = 0
	borda = [noInicio]
	while borda:
		no = borda.pop(0)
		if no.estado == META:
			sol = []
			while True:
				sol.append(no.estado)
				no = no.pai
				if not no: break
			sol.reverse()
			return sol,numerodemov
		numerodemov+=1
		if (numerodemov%(max/10))==0: print(numerodemov,end="....")
		if numerodemov>max: break
		sucessor = sucessorno(no)
		for s in sucessor:
			inserirno(criano(s,no,no.g+1),borda)				
	return 0,numerodemov

#jogo
def jogo(MaxD,numAmostras):
	tempos = []
	solucionados = []
	solucoes = []
	naosolucionados = []
	nSolucoesEncontradas = 0
	nSolucoesNaoEncontradas = 0
	for i in range(numAmostras):
		noInicio = criano(geraInicial(),None)
		iniciar_tempo = timeit.default_timer()
		res,numerodemov = buscaA(MaxD,noInicio)
		tempo = timeit.default_timer() - iniciar_tempo
		if res:
			solucoes.append(res)
			print ("\nSolucionado em {} segundos e {} movimentos" .format(tempo,numerodemov))
			tempos.append(tempo)
			solucionados.append(noInicio.estado,numerodemov)
			nSolucoesEncontradas+=1

		else:
			print("\nFalhou em {} segundos e {} movimentos " .format(tempo,numerodemov))
			naosolucionados.append(noInicio.estado,numerodemov)
			tempos.append(None)
			nSolucoesNaoEncontradas+=1
		print("solucionados {} e nao solucionados {}" .format(nSolucoesEncontradas,nSolucoesNaoEncontradas))
		return tempos,solucionados,naosolucionados,nSolucoesEncontradas,nSolucoesNaoEncontradas
		#relatorio de solucoes

def main():
	sol = jogo(3000,10) #profundidade da arvore em nos, numero de amostras aleatrorias

main()

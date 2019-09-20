import time
import timeit
import random
import copy
import math


class Noh:
	def __init__ (self,estado,nopai,g,h):
		self.estado = estado
		self.pai = nopai
		self.g = g
		self.h = h
		#cada no guarda endereco no pai, assim da pra chegar no no inicial

	def __eq__(self,outro):
		return self.estado == outro.estado

	def __repr__(self):
		return str(self.estado)
	
	#retornaestadodono
	def getState(self):
		return self.estado

class Operacoes:
	
	def __init__ (self,meta):
		self.meta = meta

	def solucionavel(self,lista):
	#Conta o numero de inversoes para ver se e solucionaval, se tiver numero de inversoo impar nao e solucionavel
	#pelo fato do incial ser par  
		inversoes = 0
		for i,e in enumerate(lista):
			if e == 0:
				continue
			for j in range(i+1,len(lista)):
				if lista[j]==0:
					continue
				if e > lista[j]:
					inversoes+=1
			if inversoes%2 == 1:
				return False
			else:
				return True

	#Gera um estado inicial diferente de META
	def geraInicial(self,st=None):
		#return [[3,7,2],[8,0,1],[4,5,6]] #--- teste com tabuleiro escolhido
		if(st == None):
			st = self.meta[:]
		lista = [j for i in st for j in i]
		while True:
			random.shuffle(lista)
			st = [lista[:3]]+[lista[3:6]]+[lista[6:]]
			if self.solucionavel(lista) and st!=self.meta: return st
		return 0

	#achar elemento no tabuleiro, por padrao acha o vazio primeiro
	def localizar(self,estado,elemento=0):
		for i in range(3):
			for j in range(3):
				if estado[i][j]==elemento:
					linha = i 
					coluna = j
					return linha,coluna

	#achar distancia quarteirao ??? de um estado/peca para outro fazendo a soma da euristica
	def distanciaQuarteirao(self,st1,st2):
		dist = 0
		fora = 0
		for i in range(3):
			for j in range(3):
				if st1[i][j]==0: continue
				i2,j2 = self.localizar(st2,st1[i][j])
				if i2 != i or j2 != j: fora += 1
				dist += abs(i2-i)+abs(j2-j)
		return dist + fora

	#cria no h = distancia percorrida + estado atual e a meta
	def criaNo(self,estado,pai,g=0):
		h = g + self.distanciaQuarteirao(estado,self.meta) #heuristica A* distancia de onde ela ta pra onde ele deve estar
		return Noh(estado,pai,g,h)

	#inserir no na fronteira e ordena pelo menor curto total
	def inserirNoh(self,no,fronteira):
		if no in fronteira:
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
	def moveAbaixo(self,estado):
		linha,coluna = self.localizar(estado)
		if linha < 2:
			estado[linha+1][coluna],estado[linha][coluna] = estado[linha][coluna],estado[linha+1][coluna]
		return estado	

	def moveAcima(self,estado):
		linha,coluna = self.localizar(estado)
		if linha > 0:
			estado[linha-1][coluna],estado[linha][coluna] = estado[linha][coluna],estado[linha-1][coluna]
		return estado		


	def moveDireita(self,estado):
		linha,coluna = self.localizar(estado)
		if coluna < 2:
			estado[linha][coluna+1],estado[linha][coluna] = estado[linha][coluna],estado[linha][coluna+1]
		return estado		


	def moveEsquerda(self,estado):
		linha,coluna = self.localizar(estado)
		if coluna > 0 :
			estado[linha][coluna-1],estado[linha][coluna] = estado[linha][coluna],estado[linha][coluna-1]
		return estado	

	#retornar todos os sucessores do eum no, estados alcansaveis 

	def sucessor(self,no):
		estado = no.estado

		listaS = []
		l1 = self.moveAcima(copy.deepcopy(estado))
		if l1 != estado:
			listaS.append(l1)
		l2 = self.moveDireita(copy.deepcopy(estado))
		if l2 != estado:
			listaS.append(l2)
		l3 = self.moveAbaixo(copy.deepcopy(estado))
		if l3 != estado:
			listaS.append(l3)
		l4 = self.moveEsquerda(copy.deepcopy(estado))
		if l4 != estado:
			listaS.append(l4)
		return listaS


	#implementar busca A*
	def busca(self,max,noInicio):
		numerodemov = 0
		borda = [noInicio]
		while borda:
			no = borda.pop(0)
			if no.estado == self.meta:
				sol =[]
				while True:
					sol.append(no.estado)
					no =no.pai
					if not no: break
				sol.reverse()
				return sol,numerodemov
			numerodemov+=1
			#if (numerodemov%(max/10))==0: print(numerodemov,end="....")
			#if numerodemov>max: break
			suc = self.sucessor(no)
			for s in suc:
				self.inserirNoh(self.criaNo(s,no,no.g+1),borda)				
		return 0,numerodemov

class Runner:
	def __init__ (self,maxD,numAmostras,entrada):
		self.maxD = maxD
		self.numAmostras = numAmostras
		self.entrada = entrada

	#jogo/main
	def run(self):
		meta = [[1,2,3],[4,5,6],[7,8,0]]
		op = Operacoes(meta)
		tempos = []
		solucionados = []
		solucoes = []
		naosolucionados = []
		nS = 0
		nNs = 0

		for i in range(self.numAmostras):
			noInicio = op.criaNo(self.entrada,None)
			start_time = timeit.default_timer()
			res,numerodemov = op.busca(self.maxD,noInicio)
			tempo = timeit.default_timer() - start_time

			if res:
				solucoes.append(res)
				tempos.append(tempo)
				solucionados.append((noInicio.estado,numerodemov))
				nS+=1
			else:
				naosolucionados.append((noInicio.estado,numerodemov))
				tempos.append(None)
				nNs+=1
			#print("solucionados {} e nao solucionados {}" .format(nS,nNs))
		
			#relatorio de solucoes
			#return tempos,solucionados,naosolucionados,nS,nNs

		return solucoes
		
#def main():
#	jogo = Jogo(5000,1,[[3,7,2],[8,0,1],[4,5,6]])
#	jogo.jogo()
#profundidade da arvore em nos, numero de amostras aleatrorias

#main()
from Fila import Fila
class Resolve():
    #algoritmo bfs do cormen, com a modificacao nas linhas 108 a 112
    #modificacao: ao visitar um no, verificar se ele eh o estado meta, se for,
    #montar a lista_solucao que eh os estados do no meta ate a raiz (percorrendo os pais)
    def __init__(self,fila,r,meta):
        self.fila = fila
        self.r = r
        self.meta = meta

    def bfs(self):
        lista_solucao = []
        self.r.cor = 'cinza'
        fila = Fila(self.r,[])
        while(not(self.fila.filavazia())):
            u = self.fila.removefila()
            if(u.value == self.meta):
                while(u != None):
                    lista_solucao.append(u)
                    u = u.pai
                return lista_solucao
            #quando um no eh visitado (retirado da fila) cria-se a lista de nos filhos dele (adjacencia / proximos estados)
            u.crialistaadj()
            for v in u.adj:
                if(v.cor == 'branco'):
                    v.cor = 'cinza'
                    self.fila.inserefila(v)
            u.cor = 'preto'
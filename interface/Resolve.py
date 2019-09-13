class Resolve():
    #algoritmo bfs do cormen, com a modificacao nas linhas 108 a 112
    #modificacao: ao visitar um no, verificar se ele eh o estado meta, se for,
    #montar a lista_solucao que eh os estados do no meta ate a raiz (percorrendo os pais)
    def bfs(self,fila,r,meta):
        lista_solucao = []
        r.cor = 'cinza'
       #fila = Fila(r)
        while(not(fila.filavazia())):
            u = fila.removefila()
            if(u.value == meta):
                while(u != None):
                    lista_solucao.append(u)
                    u = u.pai
                return lista_solucao
            #quando um no eh visitado (retirado da fila) cria-se a lista de nos filhos dele (adjacencia / proximos estados)
            u.crialistaadj()
            for v in u.adj:
                if(v.cor == 'branco'):
                    v.cor = 'cinza'
                    fila.inserefila(v)
            u.cor = 'preto'
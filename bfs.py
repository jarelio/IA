class No:
    def __init__(self,value,adj=[],cor='branco'):
        self.cor = cor
        self.adj = adj
        self.value = value

class Fila:
    def __init__(self,raiz,lista = []):
        self.lista = lista
        self.lista.append(raiz)

    def removefila(self):
        no = self.lista[0]
        self.lista.remove(no)
        return no

    def inserefila(self,no):
        self.lista.append(no)

    def retornafila(self):
        return self.lista
        
    def filavazia(self):
        return len(self.lista)==0

def bfs(r):
    r.cor = 'cinza'
    fila = Fila(r)
    while(not(fila.filavazia())):
        u = fila.removefila()
        print(u.value)
        for v in u.adj:
            if(v.cor == 'branco'):
                v.cor = 'cinza'
                fila.inserefila(v)
        u.cor = 'preto'

def main():

    no1 = No(1)
    no2 = No(2)
    no3 = No(3)
    no4 = No(4)
    no5 = No(5)
    no6 = No(6)

    lista_v1 = [no6]
    lista_v2 = [no3,no6]
    lista_v3 = [no2,no4,no6]
    lista_v4 = [no1,no5]
    lista_v5 = [no4,no6]
    lista_v6 = [no1,no4]

    no1.adj = lista_v1
    no2.adj = lista_v2
    no3.adj = lista_v3
    no4.adj = lista_v4
    no5.adj = lista_v5
    no6.adj = lista_v6

    bfs(no2)

main()
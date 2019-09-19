from Fila import Fila
from No import No
from Resolve import Resolve
values = [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
meta = [[1,2,3],[4,5,6],[7,8,0]]
no_inicial = No(values,None)
fila = Fila(no_inicial,[])
resolve = Resolve(fila,no_inicial,meta).bfs()
resolve.reverse()
for i in resolve:
    print(i.value)

values2 = [[1, 0, 3], [4, 2, 6], [7, 5, 8]]
no_inicial2 = No(values2,None)
fila2 = Fila(no_inicial2,[])
resolve2 = Resolve(fila2,no_inicial2,meta).bfs()
resolve2.reverse()
for i in resolve2:
    print(i.value)
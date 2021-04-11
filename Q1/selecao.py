from Q1.mod import lista
import time

inicio = time.time()
def SelSorting(lista='lista'):
    for t in range(len(lista)):
        minimo = t
        for k in range(t+1, len(lista)):
            if lista[minimo] > lista[k]:
                minimo = k
        lista[t], lista[minimo] = lista[minimo], lista[t]

'''SelSorting(lista)
for i in range(len(lista)):
    print(lista[i])'''

fim = time.time()
diferenca = fim - inicio
print(diferenca)



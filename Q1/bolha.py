from Q1.mod import lista

def bub_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# ********* REMOVA AS ASPAS SIMPLES PARA LER O CÓDIGO *******
''' lista_ordenada = bubble_sort(lista)
print(f'Bubble sort:   {lista_ordenada}')
'''



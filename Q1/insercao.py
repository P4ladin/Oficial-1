from Q1.mod import lista


def insert_sort(lista):
    
    n = len(lista)
    for i in range(1, n):
        insert_value = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > insert_value:
            lista[j + 1] = lista[j]

            j -= 1

        lista[j + 1] = insert_value
    return lista

#***********REMOVA AS ASPAS SIMPLES PARA LER O CODIGO********

'''lista_ordenada2 = insertion_sort(lista)
print(f'Insertion Short:   {lista_ordenada2}')'''
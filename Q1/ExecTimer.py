import time
from Q1.mod import lista
from Q1.bolha import bub_sort
from Q1.insercao import insert_sort
from Q1.selecao import  SelSorting


print("*************** Buble Sort ***************")
tempoInicial1 = time.time()
bub_sort(lista)
print('Duração: %0.5f' % (time.time() - tempoInicial1))

print("\n*************** Insertion Sort ***************")
tempoInicial2 = time.time()
insert_sort(lista)
print('Duração: %0.5f' % (time.time() - tempoInicial2))

print("\n*************** Selection Sort ***************")
tempoInicial3 = time.time()
SelSorting(lista)
print('Duração: %0.4f' % (time.time() - tempoInicial3))

'''Justifique qual teve o melhor desempenho em sua opinião.'''

''' Após devida análise em hardware mais avançado que o meu atual, 
     o que teve desempenho superior nos requisitos especificados
    foi o Insertion sort porque ele e o que apresentou
    mais rapidez em ordenar um array de 50k de numeros aleatorios
    com o menor desempenho sendo dado ao bubble sort,
    sendo que o mesmo necessitou checar repetidas vezes o array para organizar de maneira devida.
    tal fenomeno acontece devido ao uso de um algoritimo de busca linear no bubble sort.
    (para mais detalhes, vide arquivo Q2)''' 



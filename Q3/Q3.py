import csv
from collections import OrderedDict


with open ('Users\Gibraltar\Documents\GitHub\Oficial-1\Q3\cursos-prouni2.csv', "r") as arq_csv:
    lista = csv.reader(arq_csv)
    
    r = []
    [r.append(i) for i in lista if not r.count(i)]

    print(sorted(r))
    
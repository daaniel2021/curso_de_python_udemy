'''
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem Importa
Produto - Ordem importa e repete valores únicos
'''

from itertools import combinations, permutations, product

pessoas = ['Luis', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in combinations(pessoas, 3):
    print((grupo))
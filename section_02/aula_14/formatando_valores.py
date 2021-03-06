'''
Formatando valores com modificadores

:s - Texto (strings
:d - Inteiros (int)
:f - Número de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao:.2f}')
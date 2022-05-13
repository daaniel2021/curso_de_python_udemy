'''
Operadores Relacionais
== >= < <= !=

o input reotrna uma string, logo para ser obter inteiro precisa converter
'''

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
nome1 = nome.capitalize()

#  limite para pegar empréstimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome1} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')
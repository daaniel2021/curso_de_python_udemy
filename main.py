# 1 - crie uma funçao que exiba uma saudação com os parâmetros saudacao e nome

'''def saudacao(s, nome):
    nome = nome.capitalize()
    print(s, nome)

saudacao(s = 'Seja bem-vindo', nome  = input('Digite o seu nome: '))
'''

# 2 - Crie uma função que receba 3 números com parâmetros e exiba a soma entre eles.

''''def soma(n1, n2, n3):
    s = n1 + n2 + n3
    return print(s)

soma(n1 =int(input('Digite o primeiro número: ')),
    n2 = int(input('Digite o segundo número: ')),
    n3 = int(input('Digite o terceiro número: ')))'''


# 3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual ( ex. 10%). Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.

# def percentual(n, p):
#     per = n*(p/100)
#     t_per = n + per
#     return print(t_per)

# percentual(10, 10)


'''4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.'''

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'Fizz Buzz, {n} é divisível por 3 e por 5'
    if n % 3 == 0:
        return f'Fizz {n}, é divisível por 3'
    if n % 5 == 0:
        return f'buzz {n}, é divisível por 5'
    else:
         return f'{n} não é divisível nem por 3 e nem por 5.'

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
    
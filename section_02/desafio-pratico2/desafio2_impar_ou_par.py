num_int = (input('Digite um número inteiro: '))

if num_int.isdigit():
    num_int = int(num_int)

    if( num_int % 2 == 0):
        print(f'O número "{num_int}" é par')
    else:
        print(f'O número "{num_int}" é impar')
else:
    print(f'"{num_int}" não é um número')
nome = input('Informe o seu primeiro nome:')

nome_tam = len(nome)

if nome.isalpha():
    if nome_tam < 4 :
        print(f'Seu nome é muito curto')
    elif nome_tam > 6:
        print('Seu número é muito grande')
    else:
        print('Seu nome é normal ')
else:
    print('Digite um nome válido')
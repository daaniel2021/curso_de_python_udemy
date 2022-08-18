string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
numero_strings = 10
nova_string = '.'.join([string[indice:indice + numero_strings]
                        for indice in range(0, len(string), numero_strings)])
print(nova_string)

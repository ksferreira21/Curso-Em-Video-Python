# Programa de conversão de número inteiro para bin,oct e hex.
number = int(input('Digite um número inteiro: ').strip())
print(f'''{"-=-"*20}
Escolha como ele quer ser convertido: 
(1) Binário.    
(2) Octal.
(3) hexadecimal. 
{"-=-"*20}''')

resposta = int(input('Escolha o número a frente para o que você quer converter: '))
if resposta == 1:
    binario = bin(number)
    print(f'O seu número {number} convertido para binário é: {binario[2:]}')

elif resposta == 2:
    octal = oct(number)
    print(f'O seu número {number} convertido para octal é: {octal[2:]}')

elif resposta == 3:
    hexadecimal = hex(number)
    print(f'O seu número {number} convertido para hexadecimal é: {hexadecimal[2:].upper()}')

else:
    print(f'A entrada ({resposta}) é inválida!')
# Desenvolvido por Kaiky 2025

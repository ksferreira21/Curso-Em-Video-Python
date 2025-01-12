n1 = float(input('Digite qual foi sua nota na primeira prova: '))
n2 = float(input('Digite qual foi sua nota na segunda prova: '))
m = (n1 + n2) / 2
if m < 4.8:
    print(f'Sua média foi {m} e deve melhorar. Pois faltou {4.8-m:.1f} para entrar ser bom')
else:
    print(f'Sua média foi {m} e foi exelente continue assim :)')
#Media aritmética de duas notas de um aluno.
#Desenvolvido por: Kaiky Soares Ferreira
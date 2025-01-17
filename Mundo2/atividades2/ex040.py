# Programa que decide o que vai acontecer com você com base em suas notas:
nota1 = float(input('\033[34mNota da primeira prova: \033[m'))
nota2 = float(input('\033[34mNota da segunda prova: \033[m'))
media = (nota1 + nota2) / 2

print(f'\033[33mSua média foi: {media} pontos e com isso conclui-se que você está{' de:' if 5.0 <= media <= 6.9 else ':'}\033[m ')

if media >= 7.0:
    print('\033[1;32mAPROVADO!\033[m')
elif 5.0 <= media <= 6.9:
    print('\033[1;35mRECUPERAÇÃO!\033[m')
elif media < 5.0:
    print('\033[1;31mREPROVADO\033[m')
# Desenvolvido por Kaiky 2025

#Escolher o aluno:  para apagar o quadro
import random
n1 = str(input('Qual o nome do primeiro aluno: '))
n2 = str(input('Qual o nome do segundo aluno: '))
n3 = str(input('Qual o nome do terceiro aluno: '))
n4 = str(input('Qual o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O escolhido para apagar o quadro foi {escolhido}')
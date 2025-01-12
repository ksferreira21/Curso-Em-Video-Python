l = float(input('Qual é a largura da parede? '))
a = float(input('Qual é a altura da parede? '))
ar = l * a
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {ar:.1f}m².')
litros = ar / 2
print(f'Sabendo que cada litro de tinta pinta uma area de 2m², você vai precisar de {litros:.0f}l de tinta para pintar a parede toda.')
#Projeto para ajudar pintores a comprar tinta para pintar a parede.
#Desenvolvido por: Kaiky Soares Ferreira
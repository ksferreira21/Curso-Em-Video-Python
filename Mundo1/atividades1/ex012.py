pi = float(input('Qual o preço do produto? R$'))
di = float(input('Qual a porcentagem de desconto? %'))
df = di / 100
pf = pi - (df * pi)
print(f'\033[1;32mO produto que custava R${pi:.2f}, na promoção com desconto de {di:.0f}% vai custar R${pf:.2f}.\033[m')
#Projeto para ajudar pessoas a comprar produtos com desconto.
#Desenvolvido por: Kaiky 2025
# 3 segmentos de retas podem formar um triângulo?
print(f"{'-=-' * 10}\n{'Analisador de triângulos': ^30}\n{'-=-' * 10}".title())
r1 = float(input('Digite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta: '))
r3 = float(input('Digite o terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos de reta PODEM FORMAR um triângulo.')
else:
    print('Os segmentos de reta NÃO PODEM formar um triângulo.')
# Desenvolvido por Kaiky 2025

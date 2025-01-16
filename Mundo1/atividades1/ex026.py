#Vezes que aparece letra A, primeira vez, e por ultimo
frase = str(input('Digite uma frase: ').lower().strip())
print(f'''A sua frase {frase.title()} \nA letra A apareceu {frase.count('a')}x, 
A primeira vez foi na casa {frase.find('a')+1}, 
E por ultimo na casa {frase.rfind('a')+1}.''')
# Desenvolvido por Kaiky 2025

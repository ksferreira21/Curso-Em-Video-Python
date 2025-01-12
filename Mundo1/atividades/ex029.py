# Programa que calcula multa por excesso de velocidade.
km = float(input('\033[94mQual a velocidade do carro? \033[0m').replace(',', '.').strip())
if km > 80: 
    multa = (km - 80) * 7
    print(f'\033[91mVocê foi multado em R${multa:.2f} por excesso de velocidade.\033[0m')
else:
    print('\033[92mVocê está dentro do limite de velocidade por isso não foi multado.\033[0m')
print('\033[1;92mTenha um bom dia! Dirija com segurança!\033[0m')
# Developed by Kaiky 2025

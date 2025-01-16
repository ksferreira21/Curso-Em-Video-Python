from time import sleep

def mono():
    print('\033[94m' + '=' * 30 + '\033[m')
    print(f"\033[92m{'Caixa do Kaiky': ^30}\033[m")
    print('\033[94m' + '=' * 30 + '\033[m')

def carregamento():
    for i in range(4):
        print('\033[93mCarregando' + '.' * i + '\033[m', end='\r')
        sleep(1)
        print(' ' * 20, end='\r')  # Limpa a linha final

def saindo():
    for i in range(4):
        print('\033[91mSaindo' + '.' * i + '\033[m', end='\r')
        sleep(1)
        print(' ' * 20, end='\r')

def main():
    valor = float(input('\033[96mQual o valor do produto R$\033[m'))
    vista = valor - (valor * 0.1)  # Se pagar à vista terá desconto
    cartao = valor + (valor * 0.08)  # Se parcelar terá aumento

    print(f'''\033[93m{'='*15}Forma de pagamento{'='*15}\033[m
\033[93mDigite o número correspondente:\033[m
\033[92m(1) À vista.\033[m
\033[92m(2) Parcelado no cartão.\033[m
\033[91m(q) Sair\033[m''')

    resposta = input('\033[96mDigite: \033[m')
    if resposta == '1':
        carregamento()
        print(f'\033[92mO valor do produto à vista de R${valor:.2f} recebeu um desconto de 10%, \nO novo valor é de R${vista:.2f}\033[m')
    elif resposta == '2':
        carregamento()
        print(f'\033[92mO valor do produto parcelado de R${valor:.2f} recebeu um aumento de 8%, \nO novo valor a pagar é de R${cartao:.2f}\033[m')
    elif resposta == 'q':
        saindo()
    else:
        print('\033[91mEntrada Inválida!\033[m')

if __name__ == "__main__":
    mono()
    main()
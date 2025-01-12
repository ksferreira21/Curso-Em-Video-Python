# Calcula seu IMC e mostra o seus status
try:
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a seu altura: '))
    imc = peso / pow(altura, 2)

    if imc < 18.5:
        status = 'Abaixo do peso'
    elif 18.5 <= imc <= 25:
        status = 'Peso Ideal'
    elif 25 <= imc <= 30:
        status = 'Sobrepeso'
    elif 30 <= imc <= 40:
        status = 'Obesidade'
    else:
        status = 'Obesidade Mórbida'

    print(f'O seu IMC foi calculado e obteve o valor de {imc:.1f} e seu status é: {status}.')

except Exception as e:
    print(f'\033[31mPor favor, insira um ano válido.\033[m \nErro: {e}')
# Desenvolvido por Kaiky 2025

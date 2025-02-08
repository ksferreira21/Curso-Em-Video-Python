def leitor_de_dinheiro(msg):
    while True:
        number = str(input(msg))
        if number.isnumeric():
            number = float(number)
            break
        else:
            print('\033[1;31mERRO! Você não digitou um valor válido! Tente novamente.\033[m')
    return number
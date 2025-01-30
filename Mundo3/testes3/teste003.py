# Testando lista em lista :)
galera = list()
dados = list()
totmai = totmen = 0
for con in range(0,5):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    print('-=-'* 15)
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} tem {p[1]} de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maior de idade e {totmen} menor de idade')



'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} de idade')'''



'''teste = list()
teste.append('Jorge')
teste.append(16)
galera = list()
galera.append(teste[:])
teste[0] = 'Ana'
teste[1] = 33
galera.append(teste[:])
print(galera)'''

# Testado por Kaiky - 2025
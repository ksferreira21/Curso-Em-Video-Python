# Testando o dicionário!
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()



'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])
'''



'''pessoas = {'nome' : 'Kaiky',
           'Sexo' : 'M',
           'Idade' : '321'
           }
pessoas['Peso'] = 60.1
for k, v in pessoas.items():
    print(f'O {k} = {v}')

    

filme1 = {'título': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
        }
filme2 = {'título': 'Avengers',
        'ano': 2012,
        'diretor': 'Joss Whedon'
        }
filme3 = {'título': 'Matrix',
        'ano': 1999,
        'diretor': 'Wachowski'
        }
locadora = list()
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(locadora[2]['título'])'''
# Testado por Kaiky - 2025

# Programa que analisa notas de uma turma, e pode ou não mostrar a situação que se encontram.
def notas(*num, sit=False): 
    """
    -> Analisa notas de alunos e retorna um dicionário com estatísticas.

    Parâmetros:
        * num (float): Uma ou mais notas dos alunos.
        * sit (bool, opcional): Se True, adiciona a situação do aluno com base na média.

    Retorno:
        dict: Um dicionário contendo:
            - Quantidade de notas
            - Maior nota
            - Menor nota
            - Média das notas
            - Situação (opcional, caso sit=True)
    Press (q) to exit.
    """
    dados = {
        'Quantidade de notas': len(num),
        'Maior nota': max(num),
        'Menor nota': min(num),
        'Média das notas': sum(num) / len(num)
    }
    
    if sit:
        if dados['Média das notas'] >= 7:
            dados['SITUAÇÃO'] = 'Aprovado!'
        elif 5 <= dados['Média das notas'] < 7:
            dados['SITUAÇÃO'] = 'Pode melhorar...'
        else:
            dados['SITUAÇÃO'] = 'Péssimo...!'

    return dados


# Programa principal.
os_dados = notas(5.8, 3.5, 7.5, 9.6, sit=True)
print(f'\033[33m{os_dados}\033[m')
print()
ajuda = str(input('Precisa de ajuda para entender? [S/N] '))
if ajuda in 'sS':
    help(notas)
# Desenvolvido por Kaiky - 2025

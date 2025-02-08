# Programa que analisa sua idade e retorna se é obrigatório, opcional ou não permitido
def voto(ano_nascimento):
    from datetime import datetime

    idade = datetime.now().year - ano_nascimento
    if idade < 16:
        return idade, "NÃO PERMITIDO"
    
    elif 16 <= idade < 18 or idade >= 70:
        return idade, "OPCIONAL"
    
    elif idade >= 18:
        return idade, "OBRIGATÓRIO"

ano = int(input('Em que ano você nasceu? '))
idade, tipo_voto = voto(ano)

print(f'Você tem {idade} anos, e o seu voto é {tipo_voto}.')
# Desenvolvido por Kaiky - 2025

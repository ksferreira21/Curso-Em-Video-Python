# Programa que testa se o site está acessível pelo computador usando a biblioteca: urllib
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br', timeout=5)
except Exception as e:
    if e.__cause__ == None:
        print(f'\033[1;31mOcorreu um erro ao se conectar com o site. \033[35m(Verifique sua conexão e tente novamente!)\033[m')
    else:
        print(f'\033[1;31mOcorreu um erro: {e}\033[m')
else:
    print('\033[1;32mConexão estabelecida! \033[1;33m(Tudo nos conformes com o site pudim.)\033[m')
# Desenvolvido por Kaiky - 2025

m = float(input('\033[34mDigite em metros um número:\033[m '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'Em quilômetros: \033[35m{km}km\033[m \nEm hectômetros: \033[36m{hm}hm\033[m \nEm decâmetros: \033[33m{dam}dam\033[m \nEm decímetros: \033[32m{dm:.0f}dm\033[m \nEm centímetros: \033[31m{cm:.0f}cm\033[m \nEm milímetros: \033[32m{mm:.0f}mm\033[m')
# Convertor de m para km, hm, dam, dm, cm e mm
# Desenvolvido por: Kaiky Soares Ferreira
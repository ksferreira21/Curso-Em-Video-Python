import math
ang = float(input('Digite o valor do ângulo: °'))
ang_rad = math.radians(ang)
seno = math.sin(ang_rad)
cosseno = math.cos(ang_rad)
tangente = math.tan(ang_rad)
print(f'''O ângulo de {ang}° tem o SENO de {seno:.2f}
O ângulo de {ang}° tem o COSSENO de {cosseno:.2f}
O ângulo de {ang}° tem a TANGENTE de {tangente:.2f}''')
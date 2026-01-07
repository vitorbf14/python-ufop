import math

a = float(input('Informe a altura da torre (em metros): '))
e = float(input('Informe o ângulo de elevação do Sol (em graus): '))

tan = e * math.pi / 180
s = a / math.tan(tan) 

print(f'A sombra projetada no sol mede {s:.3f} metros')
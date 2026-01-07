import math

c0 = float(input('Informe a concentração inicial (em ppm): '))
t = int(input('Informe o tempo decorrido (em horas):  '))

ct = c0 / (1 + math.log10(t + math.e))

print(f'A concentração atual de poluentes é:{ct:.4f} ppm')
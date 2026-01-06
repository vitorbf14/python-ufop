k = float(input('Digite a constante elástica da mola: '))
x = float(input('Digite a extensão da mola: '))
m = float(input('Digite a massa do corpo: '))

F = k * x
a = F / m

print(f'Aceleração do corpo: {a}')


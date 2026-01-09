a = float(input('Digite a altura: '))
s = input('Digite o sexo (m ou  f): ')

if s == 'm':
    peso_ideal = (72.7 * a) - 58
elif s== 'f':
    peso_ideal = (62.1 * a) - 44.7
else:
    print('Sexo inválido. Digite "m" ou "f".')

print(f'O peso ideal é {peso_ideal:.2f} kg.')

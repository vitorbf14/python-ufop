c = float(input('Informe o capital inicial: '))
j = float(input('Informe a taxa de juros anual (em %): '))
a = int(input('Informe o número de anos: '))

m = c * ((1 + j / 100 ) ** a)

print(f'O montantte final é: {m:.2f}}')
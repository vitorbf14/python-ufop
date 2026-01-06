p = float(input('Digite seu peso (em kg): '))
a = float(input('Digite sua altura (em metros): '))
c = float(input('Digite a circunferência do seu quadril (em cm): '))

imc = p / (a ** 2)
iac = (c / (a ** 1.5)) - 18

print(f'IMC = {imc}')
print(f'IAC = {iac}')



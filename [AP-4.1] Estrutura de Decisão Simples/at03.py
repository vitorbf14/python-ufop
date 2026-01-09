nome = input('Entre com o nome: ')
idade = float(input('Entre com a idade: '))
sexo = input('Entre com o sexo(m ou f): ')

if sexo == 'm':
    maioridade = 18
elif sexo == 'f':
    maioridade = 21
else:
    print('Sexo inválido!')

if idade >= maioridade:
    print(f'{nome} tem maioridade civil')
else:
    faltam = maioridade - idade
    print(f'Faltam {faltam:.2f} anos para {nome} atingir a maioridade')

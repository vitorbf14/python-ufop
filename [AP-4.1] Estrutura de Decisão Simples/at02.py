import math

l = input('Forneça o tipo de ladrinho (g ou p): ')
a = int(input('Forneça a área da sala: '))

if l == 'g':
    area_ladrinho = 80
elif l == 'p':
    area_ladrinho = 60
else:
    print('Tipo inválido!')

q = math.ceil (a/area_ladrinho)

print(f'Quantidade de ladrinhos: {q}')



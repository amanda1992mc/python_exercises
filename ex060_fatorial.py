#calculo fatorial de um número

n = int(input("Digite um número para ver seu cálculo fatorial: "))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c -= 1
print(f)





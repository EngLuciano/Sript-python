print('\033[31m=\033[m'*261)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*261)
print('\033[30mPROGRAMA DE TABUADA COM FOR\033[m')
print('='*261)
num = int(input('Digite um Número : '))

for c in range(1, 11):
    print('{} x {:2} = {} '.format(num, c, num*c))

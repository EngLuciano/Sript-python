print('\033[31m=\033[m'*300)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*300)
print('Olá esse programa vai ajudar voçê a calcular a sua nota nas Provas')
materia = (input('Digite o Nome da Matéria : ')).capitalize()
peso1 = float(input('Digite o peso da P1 : '))
peso2 = float(input('Digite O peso da P2 : '))
pesoprev = float(input('Digite o peso as prévias :'))
##pesotrab = str(input('Sua Matéria tem algum trabalho que vale nota ? [S] ou [N] : ')).upper()

'''if pesotrab =="S":
    pesotrab2 = float(input('Digite o Peso do Trabalho : '))
    media = (nota1 * (peso1 / 100)) + (nota2 * (peso2 / 100)) + (notaprevi * (pesoprev / 100) + notatrab * (pesotrab2 / 100))

else:
   '''

nota1 = float(input('Digite a nota da P1 : '))
nota2 = float(input('Digite a nota da P2 : '))
notaprevi = float(input("Digete sua nota nas Prévias : "))
notatrab = float(input("Digite a Nota do Trabalho : "))
media = (nota1 * (peso1 / 100)) + (nota2 * (peso2 / 100)) + (notaprevi * (pesoprev / 100))

if media >= 7 and pesotrab =="S":

    print('Aprovado ')
else:
    print('Reprovado')



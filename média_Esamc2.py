print('\033[31m=\033[m'*300)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*300)
print('\033[30mOlá esse programa vai ajudar voçê a calcular a sua nota nas Provas\033[m')
nome = str((input('Nome do Aluno : '))).capitalize().upper()
materia = (input('Digite o Nome da Matéria : ')).capitalize().upper()
peso1 = float(input('Digite o peso da P1 : '))
peso2 = float(input('Digite O peso da P2 : '))
pesoprev = float(input('Digite o peso as prévias :'))
pesotrab = str(input('Sua Matéria tem algum trabalho que vale nota ? [S] ou [N] : ')).upper()

if pesotrab =="S":
    pesotrab2 = float(input("Digite o Peso do Trabalho : "))
    notatrab = float(input('Digite a Nota do Trabalho : '))
else:
    print()

nota1 = float(input('Digite a nota da P1 : '))
nota2 = float(input('Digite a nota da P2 : '))
notaprevi = float(input("Digite sua nota de Prévias : "))



if pesotrab =="S":
    media = (nota1 * (peso1 / 100)) + (nota2 * (peso2 / 100)) + (notaprevi * (pesoprev / 100)) + (notatrab * (pesotrab2 / 100))

else:
    media = (nota1 * (peso1 / 100)) + (nota2 * (peso2 / 100)) + (notaprevi * (pesoprev / 100))

if media >= 7:
    exibi = "Aprovado"
    print('O aluno {} teve Média de {:.2f} está {} : '.format(nome, media, exibi))
else:
    exibi = 'Reprovado'
    print('O aluno {} teve Média de {:.2f} e está {} : '.format(nome, media, exibi))


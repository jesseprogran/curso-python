
n1 = n2 = 0
media = 0

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

#calucular média aritimética das notas
media = (n1 + n2) / 2

if (media >= 7):
    print('Voçê foi aprovado')
    print('Parabéns...^^')
elif (media >= 5):
    print('Aluno em Recuperação..')    
else:
    print('Voçê Foi Reprovado')

print('Sua Média é {}'.format(media))

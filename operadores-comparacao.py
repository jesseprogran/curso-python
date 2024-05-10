# == igual a
# != diferente de 
# > maior que
# > menor  que
# >= maior ou igual a
# <= menor ou igual a

x = y = t = z = False
n1 = n2 = 0

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

x = n1 == n2
print('São iguais? ', x, '\n')

z = n1 > n2 
print(n1, ' é maior que ', n2, '? ', z, '\n')
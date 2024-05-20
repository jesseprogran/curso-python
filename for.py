# lista = ['bolo', 'melão','melancia',1,13,30]
# for item in lista:
#     print(lista)

# for numero in range(1,101):
#     print(f'o numero é {numero}')


# nome = input('Digite seu nome:')
# for x in range(10):
#     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)
# for x in range(2,40,2):
#      print(x)


# times_serie_a = ('São Paulo','Palmeira','Flamengo','Cruzeiro','Bahia')
# for times in times_serie_a:
#     if times == 'Cruzeiro':
#         continue
#     print(times)


notas = []

while True:
    nota = int(input('Digite uma nota ou -1 para sair: '))
    if nota == -1:
        break
    notas.append(nota)


soma = 0

for i in notas:
    soma = soma + i

media = soma / len(notas)
print(media)     
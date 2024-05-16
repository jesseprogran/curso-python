# nome = None

# while True:
#     print('Digite seu nome, ou x para parar:')
#     nome = input()
#     if nome == 'x' or nome == 'x':
#         break
#     print(f'Bem Vindo, {nome}')
# print('Até logo!')    


somatorio = 0

while True:
    somatorio += 1
    print(somatorio)
    
    res = str(input('Quer continuar? [s/n]')).lower()
    if res == 'n':
        break
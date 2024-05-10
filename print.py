#Sintaxe:
#print(objetos, argumentos)

nome = input('Digite seu nome: ')
msg = 'Olá ' + nome + ', Seja bem vindo ao curso de pyuthon.'
print(msg)

name = 'Jessé'
age = 33
msg_formatada = 'o nome dele é {0} e ele tem {1} anos'.format(name,age)
print(msg_formatada)



peso = 111
altura = 1.75

mensagem = f'Olá, me chamo {name}, tenho {age} anos meu peso atual é de {peso}kg e minha atura é de {altura}'
print(mensagem)
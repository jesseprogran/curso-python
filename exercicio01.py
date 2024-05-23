#01 - FAÇA UM PROGRAMA QUE LEIA 4 NOTAS, MOSTRE AS NOTAS E A MÉDIA NA TELA.
# nota_um = float(input('Digite a primeira Nota: '))
# print(nota_um)
# nota_dois = float(input('Digite a seunda Nota: '))
# print(nota_dois)
# nota_tres = float(input('Digite a terceira  Nota: '))
# print(nota_tres)
# nota_quarta = float(input('Digite a quarta Nota: '))
# print(nota_quarta)

# media = (nota_um + nota_dois + nota_tres + nota_quarta) / 2
# print(f'a média final foi {media}')


#02- descubra o servidor do email, pegar o 1 nome do usuario,
# construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso e o email tal
# construa uma mensagem: Enviamos um link de confirmação para o email j***@gmail.com
nome = 'Jessé Pereira da Silva'
email = 'jessecode22@gmail.com'

posicao = email.find('@')
servidor = email[posicao:]
print(servidor)

posicao = nome.find(' ')
primeiro_nome = nome[:posicao]
print(primeiro_nome)

mensagem = f' Usuário {primeiro_nome} cadastrado com sucesso com o email {email}'
print(mensagem)

primeira_letra = email[0]
mensagem2 = f'Enviamos um link de confirmação para o email {primeira_letra}***{servidor}'
print(mensagem2)
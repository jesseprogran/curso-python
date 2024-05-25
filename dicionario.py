# pessoa = {
#     'nome': 'Jessé Silva',
#     'idade':32,
#     'cidade': 'Icapuí'
# }

# print(pessoa['nome'])



# carro = [{'nome':'Gol', 'ano':1991, 'fabrica':'CE'}, {'nome':'Fiat', 'ano':2001, 'fabrica':'RS'}]

# print(carro[1]['nome'])


# Exercicio 
dic_preco = {
    'celular':1500,
    'camera':1000,
    'fone de ouvido':800,
    'monitor':2000
}

produtos_procurados = input('Digite um produto:')
produtos_procurados = produtos_procurados.lower()

if produtos_procurados in dic_preco:
    posicao = dic_preco[produtos_procurados]
    print(f'Produto: {produtos_procurados}, Preços: {posicao}')
else:
    print('Produto não cadastrado, tente novamente...')    
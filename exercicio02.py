# Crie um sistema de consulta de preço;
precos = [1500, 1000, 800, 2000]
produtos = ['celular', 'camera', 'fone de ouvido', 'monitor']
produtos_procurados = input('Digite um produto:')
produtos_procurados = produtos_procurados.lower()

if produtos_procurados in produtos:
    posicao = produtos.index(produtos_procurados)
    preco = precos[posicao]
    print(f'Produto: {produtos_procurados}, Preço: {preco}')
else:
    print('Produto não encontrado, tente novamente.')    

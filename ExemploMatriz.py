produtos = []

while True:
    nome = input("Nome do Produto: ")
    preco = int (input('Preço: '))
    categoria = input('Categoria: ')
    produtos.append( [nome,  preco, categoria] )
    r = input("Deseja continuar? ")
    if r=='n' or r=='N':
        break

for i in produtos:
    print(f''' Produto: {i[0]} - Preco: R${i[1]}
           , Categoria: {i[2]}''') 

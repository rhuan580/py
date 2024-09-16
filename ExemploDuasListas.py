listaProduto = []
listaPreco = []

while True:
    nome = input("Nome do Produto: ")
    preco = input('Preço: ')
    listaProduto.append(nome)
    listaPreco.append(preco)
    r = input("Deseja continuar? ")
    if r in 'N':
        break

for n in listaProduto:
    print(n)

for i in listaPreco:
    print(i)

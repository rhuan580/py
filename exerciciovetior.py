numeros = []  
while True:
     numero = float(input("Digite um número (ou 0 para sair): "))
     if numero == 0:
         break
     soma = 0
     numeros.append(numero)
     print("Por favor, digite um número válido.")
     if numeros:
        soma = sum(numeros)
        media = soma / len(numeros)
        quantidade = len(numeros)
        print(f"Soma dos números: {soma:.2f}")
        print(f"Média dos números: {media:.2f}")
        print(f"Quantidade de números: {quantidade}")
     else:
        print("Nenhum número foi digitado.)")

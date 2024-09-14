def ler_precos():
    """Lê preços de produtos do usuário e retorna uma lista com os preços."""
    precos = []
    while True:
        while True:
            try:
                preco = float(input("Digite o preço do produto (ou um valor negativo para encerrar): R$"))
                if preco < 0:
                    return precos
                precos.append(preco)
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número válido.")
        continuar = input("Deseja adicionar outro preço? (s/n): ").strip().lower()
        if continuar != 's':
            return precos

def calcular_estatisticas(precos):
    """Calcula a quantidade de produtos abaixo de R$50,00 e a média dos preços acima de R$100,00."""
    abaixo_50 = sum(1 for preco in precos if preco < 50)
    acima_100 = [preco for preco in precos if preco > 100]
    
    if acima_100:
        media_acima_100 = sum(acima_100) / len(acima_100)
    else:
        media_acima_100 = 0
    
    return abaixo_50, media_acima_100

def main():
    precos = ler_precos()
    abaixo_50, media_acima_100 = calcular_estatisticas(precos)
    
    print(f"Quantidade de produtos com preço inferior a R$50,00: {abaixo_50}")
    print(f"Média dos preços dos produtos com preço superior a R$100,00: R${media_acima_100:.2f}")

if __name__ == "__main__":
    main()

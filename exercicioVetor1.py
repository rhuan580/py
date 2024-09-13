def ler_vetor(tamanho):
    """Lê um vetor de números inteiros do tamanho especificado."""
    vetor = []
    print(f"Digite {tamanho} números inteiros:")
    for i in range(tamanho):
        while True:
            try:
                valor = int(input(f"Digite o número {i+1}: "))
                vetor.append(valor)
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número inteiro.")
    return vetor

def calcular_pares_impares(vetor):
    """Calcula e retorna a quantidade de números pares, ímpares e uma lista de ímpares."""
    quantidade_pares = 0
    quantidade_impares = 0
    impares = []
    
    for numero in vetor:
        if numero % 2 == 0:
            quantidade_pares += 1
        else:
            quantidade_impares += 1
            impares.append(numero)
    
    return quantidade_pares, quantidade_impares, impares

def main():
    tamanho_vetor = 6
    vetor = ler_vetor(tamanho_vetor)
    quantidade_pares, quantidade_impares, impares = calcular_pares_impares(vetor)
    
    print(f"Quantidade de números pares: {quantidade_pares}")
    print(f"Quantidade de números ímpares: {quantidade_impares}")
    print(f"Números ímpares: {impares}")

if __name__ == "__main__":
    main()

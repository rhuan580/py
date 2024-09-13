# Função para ler um vetor de 15 posições
def ler_vetor(tamanho):
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

# Função para multiplicar todos os elementos do vetor por 3
def multiplicar_por_tres(vetor):
    return [x * 3 for x in vetor]

# Função principal
def main():
    tamanho_vetor = 15
    vetor = ler_vetor(tamanho_vetor)
    vetor_multiplicado = multiplicar_por_tres(vetor)
    print("Vetor após multiplicar todos os elementos por 3:")
    print(vetor_multiplicado)

# Chama a função principal
if __name__ == "__main__":
    main()

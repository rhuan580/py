vetor = []
for i in range (6):
    numero = int(input("Informe número: "))
    vetor.append(numero)
quantPares = 0
quantImpares = 0
for elemento in vetor:
    if elemento % 2 == 0:
        quantPares = quantPares + 1
    else:
        quantImpares = quantImpares + 1
        print(elemento)

print(f"Quantidade de pares: ", {quantPares})
print(f"Quantidade de impares: ", {quantImpares})

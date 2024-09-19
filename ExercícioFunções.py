class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    return Aluno(nome, nota1, nota2)


def relatorio_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nRelatório de Alunos:")
        for aluno in alunos:
            print(f"Nome: {aluno.nome}, Nota 1: {aluno.nota1}, Nota 2: {aluno.nota2}, Média: {aluno.media():.2f}")


def main():
    alunos = []
    
    while True:
        print("\nMenu:")
        print("1 - Cadastro")
        print("2 - Relatório")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            aluno = cadastrar_aluno()
            alunos.append(aluno)
            print(f"Aluno {aluno.nome} cadastrado com sucesso!")

        elif opcao == '2':
            relatorio_alunos(alunos)

        elif opcao == '0':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

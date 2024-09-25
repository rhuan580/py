import mysql.connector
try:
 conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database='escola'
)

 cursor = conexao.cursor()

 nome = input("Informe o nome: ")
 nota1 = float(input("Informe a nota 1: "))
 nota2 = float(input("Informe a nota 2: "))

 sql = "INSERT INTO alunos (nome, nota1, nota2) VALUES (%s, %s, %s)"
 valores = (nome, nota1, nota2)
 cursor.execute(sql, valores)

 conexao.commit()

 cursor.close()
 conexao.close()

except:
    print("Erro ao cadastrar")

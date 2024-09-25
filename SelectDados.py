import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database='escola'
)

cursor = conexao.cursor()

nome = input("Nome: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
sql = "INSERT INTO alunos (nome, nota1, nota2) VALUES (%s, %s, %s)"
valores = (nome, nota1, nota2)
cursor.execute(sql, valores)

conexao.commit()

cursor.close()
conexao.close()

sql = """select * from alunos order by nome"""
cursor.execute(sql)
resultado = cursor.fetchall()
cursor.close()
conexao.close()

for r in resultado:
    print(r)

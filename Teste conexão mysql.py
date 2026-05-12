import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="floricultura",
    port=3307
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM cliente")

dados = cursor.fetchall()

for clientes in dados:
    print(clientes)
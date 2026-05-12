from mainSql import conexao

cursor = conexao.cursor()

cursor.execute("SELECT * FROM cliente")

dados = cursor.fetchall()

for dado in dados:
    print(dado)
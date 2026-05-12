from mainSql import conexao

cursor = conexao.cursor()

sql = "INSERT INTO cliente (nome_cliente) values (%s)"

valores = ("Douglas",)

cursor.execute(sql, valores)

conexao.commit()

print("CLIENTE CADASTRADO COM SUCESSO")



from mainSql import conexao

cursor = conexao.cursor()

valores = ("Douglas Gustavo dos Santos Braga", 1)

update = "UPDATE cliente SET nome_cliente = %s WHERE idCliente = %s"

cursor.execute(update, valores)

conexao.commit()

print("Cliente atualizado com sucesso!")
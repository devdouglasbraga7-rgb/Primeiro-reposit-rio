from mainSql import conexao

cursor = conexao.cursor()

sql = "DELETE FROM cliente WHERE idcliente = %s"

valor = (3,)

cursor.execute(sql, valor)

conexao.commit()

print("Cliente deletado com sucesso!")
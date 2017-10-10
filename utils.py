## modulo responsavel por fazer a conexao com o BD e executar as transacoes.
import sqlite3

class Connector:
	def __init__(self, bd_name):
		con = sqlite3.connect(bd_name + '.db')
		self.cursor = con.cursor()


	def create_table(self, table_name, fields):
		sql = 'create table {} ('.format(table_name)

		for field in fields:
			sql += (field + ', ')

		sql = sql[:len(sql)-2]
		sql += ")"

		print(sql)

		self.cursor.execute(sql)			



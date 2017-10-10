## modulo responsavel por fazer a conexao com o BD e executar as transacoes.
import sqlite3

class Connector:
	def __init__(self, bd_name):
		self.con = sqlite3.connect(bdname + '.db')
		self.cursor = con.cursor()


	def create_table(self, table_name, fields):
		sql = 'create table {} ('

		for field in fields:
			sql += (field + ', ')

		sql = sql[:len(sql)-1]
		sql += ")"

		self.cursor.execute(sql)			



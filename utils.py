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
		
		self.cursor.execute(sql)			

	def insert(self, fields):		
		sql = 'insert into cliente values (?,?)'		
		self.cursor.execute(sql, fields)





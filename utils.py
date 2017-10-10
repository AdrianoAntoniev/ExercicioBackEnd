from customer import Customer
import sqlite3

class DBHandler:
	def __init__(self):		
		self.database = 'processo_valemobi.db'
		self.table_name = 'tb_customer_account'
		self.con = None					

	def connect(self):
		self.con = sqlite3.connect(self.database)

	def create_table(self):
		## VERIFICAR SE EXISTE UM COMANDO con.isOpen()... if self.con.		
		cursor = self.con.cursor()
		sql = 'create table if not exists {}(id_customer integer primary key autoincrement, '\
											   'cpf_cnpj number(18,0), '\
											   'nm_customer varchar(40), '\
											   'is_ative number(1,0), '\
											   'vl_total number(10,2))'.format(self.table_name) 
					
		cursor.execute(sql)
		##self.con.close()


	def insert(self, customer):
		cursor = self.con.cursor()
		sql = 'insert into {} values (null, ?, ?, ?, ?)'.format(self.table_name)		

		values = (customer.get_cpf_cnpj(), customer.get_nm_customer(), 
			customer.get_is_active(), customer.get_vl_total())

		cursor.execute(sql, values)
		self.con.commit()


	def insert_all(self, customers):
		for customer in customers:
			self.insert(customer)



	def select_by_id(self, id):		
		sql = 'select * from {} where id_customer = {}'.format(self.table_name, id)				
		return self._fetch(sql)



	def select_by_name(self, name):		
		sql = "select * from {} where nm_customer = \'{}\'".format(self.table_name, name)
		print(sql)
		return self._fetch(sql)

	def select_all(self):		
		sql = 'select * from {}'.format(self.table_name)		
		return self._fetch(sql)
	
	## this function should be used in order to eliminate duplicate code.	
	## python does not provide access modifiers =/
	def _fetch(self, sql, delete=False):
		cursor = self.con.cursor()
		cursor.execute(sql)
		
		if not delete:
			data = cursor.fetchall()
			return data
		return True

	def delete_id(self, id):
		sql = 'delete from {} where id_customer = {}'.format(self.table_name, id)
		return self._fetch(sql, delete=True)

	def delete_name(self, name):
		sql = "delete from {} where nm_customer = \'{}\'".format(self.table_name, name)		
		return self._fetch(sql, delete=True)	



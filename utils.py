from customer import Customer
import sqlite3

class DBHandler:
	def __init__(self):		
		self.database = 'CUSTOMERS.db'
		self.table_name = 'tb_customer_account'
		self.connection = None					

	def connect(self):
		self.connection = sqlite3.connect(self.database)

	def create_table(self):		
		cursor = self.connection.cursor()
		sql = 'drop table if exists {}'.format(self.table_name)
		cursor.execute(sql)
		sql = 'create table if not exists {}(id_customer integer primary key autoincrement, '\
											   'cpf_cnpj number(18,0), '\
											   'nm_customer varchar(40), '\
											   'is_active number(1,0), '\
											   'vl_total number(10,2))'.format(self.table_name) 
					
		cursor.execute(sql)		

	def insert(self, customer):
		cursor = self.connection.cursor()
		sql = 'insert into {} values (null, ?, ?, ?, ?)'.format(self.table_name)		

		values = (customer.get_cpf_cnpj(), customer.get_nm_customer(), 
			customer.get_is_active(), customer.get_vl_total())

		cursor.execute(sql, values)
		self.connection.commit()


	def insert_all(self, customers):
		for customer in customers:
			self.insert(customer)


	def get_total_sum_and_customers_based_in(self, value, interval):	
		inner_inner_sql = 'select * from {} where vl_total > {}'.format(self.table_name, value)				
		inner_sql = 'select * from ({}) where id_customer > {} and id_customer < {} order by vl_total desc'.format(inner_inner_sql, interval[0], interval[1])

		filtered_customers = self._fetch(inner_sql)
		
		sql = "select (sum(vl_total) / count(*)) from ({})".format(inner_sql)		
		media = self._fetch(sql)				 
		
		return {'customers': filtered_customers, 'media': media}

	## this function should be used in order to eliminate duplicate code.	
	## python does not provide access modifiers =/ 	
	def _fetch(self, sql):
		cursor = self.connection.cursor()
		cursor.execute(sql)			
		return cursor.fetchall()			


	def close_connection(self):
		self.connection.close()

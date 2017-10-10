## classe de entidade

class Customer:
	def __init__(self, cpf_cnpj, nm_customer, is_active, vl_total):
		self.cpf_cnpj = cpf_cnpj
		self.nm_customer = nm_customer
		self.is_active = is_active
		self.vl_total = vl_total

	def get_cpf_cnpj(self):
		return self.cpf_cnpj

	def get_nm_customer(self):
		return self.nm_customer

	def get_is_active(self):
		return self.is_active 

	def get_vl_total(self):
		return self.vl_total
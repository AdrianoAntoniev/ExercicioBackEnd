## classe de entidade

class Customer:
	def __init__(self, cpf_cnpj, nm_customer, is_active, vl_total):
		self.cpf_cnpj = cpf_cnpj
		self.nm_customer = nm_customer
		self.is_active = is_active
		self.vl_total = vl_total
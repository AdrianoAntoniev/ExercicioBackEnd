from utils import * 
from customer import Customer
import string
from random import randint

handler = DBHandler()		 
handler.connect()
handler.create_table()

def insert_customer(cpf, name, active, total_value):
	c = Customer(cpf, name, active, total_value)	
	handler.insert(c)	

def do_search():
	return handler.get_total_sum_and_customers_based_in(value=560.00, interval=(1500, 2700))


names = ['Joao', 'Augusto', 'Maria', 'Pedro', 'Radames', 
		 'Severino', 'Arnold', 'Joana', 'Camila', 'Angelica',
		 'Andre', 'Jeniffer', 'Paola', 'Otavio', 'Tarcisio']

second_names = ['Rodrigues', 'Souza', 'Ferreira', 'Lopes', 'Benevides',
				 'Schneider', 'Buarque', 'Smith', 'Sato', 'Abdalla',
				 'Vieira', 'Knitell', 'Bach', 'Cobain', 'Pereira']

last_names = ['dos Santos', 'da Silva', 'von Neumann', 'de Alencar', 'de Paiva',
			  'da Villa', 'Nunes', 'Facchini', 'Bhaskara', 'Lennon',
			  'Zuckerberg', 'Stradivarius', 'Klinsmann', 'McDonald', 'Kong']				


for i in range(1, 3001):
	x,y,z = randint(0,14), randint(0,14), randint(0,14)

	name = "{} {} {}".format(names[x], second_names[y], last_names[z])		
	value = (randint(100, 99999)) / 100.00
	rg = randint(11111111111, 99999999999)
	active = randint(0,1)
	
	insert_customer(rg, name, active, value)


dict_customers_and_media = do_search()

print('______________________________________________________________________________________________________________')
for customer in dict_customers_and_media['customers']:	
	print('id: %4d | cpf: %11d | nome: %33s | ativo?: %3s | saldo total: %10.2f |' 
		% (customer[0], customer[1], customer[2], 'sim' if customer[3] else 'nao', customer[4])) 
	print('______________________________________________________________________________________________________________')

print('______________________________________________________________________________________________________________')
print("Media geral de saldo dos clientes com ID entre 1500 e 2700: %10.2f" % dict_customers_and_media['media'][0])













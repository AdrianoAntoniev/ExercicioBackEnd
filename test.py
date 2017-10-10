from utils import * 
from customer import Customer
import string
from random import randint

handler = DBHandler()		 
handler.connect()
handler.create_table()

def inserindo_contato(cpf, nome, ativo, valor_total):
	cliente = Customer(cpf, nome, ativo, valor_total)	
	handler.insert(cliente)	

def busca_valor_maior_que_560_entre_1500_e_2700_com_media():
	return handler.get_total_sum_and_customers_based_in(560.00, (1500, 2700))


nomes = ['Joao', 'Augusto', 'Maria', 'Pedro', 'Radames', 
		 'Severino', 'Arnold', 'Joana', 'Camila', 'Angelica',
		 'Andre', 'Jeniffer', 'Paola', 'Otavio', 'Tarcisio']

nomes_do_meio = ['Rodrigues', 'Souza', 'Ferreira', 'Lopes', 'Benevides',
				 'Schneider', 'Buarque', 'Smith', 'Sato', 'Abdalla',
				 'Vieira', 'Knitell', 'Bach', 'Cobain', 'Pereira']

nome_final = ['dos Santos', 'da Silva', 'von Neumann', 'de Alencar', 'de Paiva',
			  'da Villa', 'Nunes', 'Facchini', 'Bhaskara', 'Lennon',
			  'Zuckerberg', 'Stradivarius', 'Klinsmann', 'McDonald', 'Kong']				

for i in range(1, 3001):
	x,y,z = randint(0,14), randint(0,14), randint(0,14)

	nome = "Cliente {} {} {}".format(nomes[x], nomes_do_meio[y], nome_final[z])		
	valor = (randint(100, 99999)) / 100.00
	rg = randint(11111111111, 99999999999)
	ativo = randint(0,1)
	
	inserindo_contato(rg, nome, ativo, valor)


r = busca_valor_maior_que_560_entre_1500_e_2700_com_media()

print("Clientes...")
for customer in r['customers']:
	print(customer)

print("Media ", r['media'])













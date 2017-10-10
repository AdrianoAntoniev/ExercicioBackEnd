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

	#handler.insert_all([michel, dilma])

def busca_todos():	
	return  handler.select_all()

def busca_valor_maior_que_560_entre_1500_e_2700():
	return handler.select_larger_than_and_id_in(560.00, (15, 27))

def busca_valor_maior_que_560_entre_1500_e_2700_com_media():
	return handler.select_name_and_value_total_and_count(560.00, (15, 27))



alfabeto1 = list(string.ascii_lowercase[:])
alfabeto2 = list(string.ascii_uppercase[:])
numeros = list(range(1, 27))

for i in range(1, 401):
	x,y,z = randint(1,25), randint(1,25), randint(1,25)

	nome = "Senhor {}{}{}".format(alfabeto1[x], alfabeto2[y], numeros[z])	
	valor = (randint(100, 99999)) / 100.00
	rg = randint(11111111111, 99999999999)
	ativo = randint(0,1)
	
	inserindo_contato(rg, nome, ativo, valor)


r = busca_valor_maior_que_560_entre_1500_e_2700_com_media()

print("Clientes...")
for customer in r['customers']:
	print(customer)

print("Media ", r['media'])













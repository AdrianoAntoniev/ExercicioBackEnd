from utils import * 
from customer import Customer


handler = DBHandler()		 
handler.connect()
handler.create_table()

paulo = Customer(12222212222, 'Paulo Maluf', 1, 9999999.00)
handler.insert(paulo)
michel = Customer(22222222222, 'Michel Temer', 1, 9999999999.00)
dilma = Customer(33333333333, 'Dilma Rousseff', 1, 9999999999.12)

handler.insert_all([michel, dilma])

print("Verificando se o programa deu certo...\nSelecionando toda a corja:")

def printing():
	resps = handler.select_all()
	for resp in resps:
		print(resp)

printing()
print("Agora selecionando o numero 1 da lista:")
print(handler.select_by_id(1))


print("Agora selecionando nossa querida dilminha...")
print(handler.select_by_name('Dilma Rousseff'))

print("Agora deletando o Michel Temer.")
handler.delete_id(2)
printing()

print("Deletando Paulo Maluf.")
handler.delete_name('Paulo Maluf')
printing()






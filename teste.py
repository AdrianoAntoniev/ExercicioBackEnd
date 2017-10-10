## Classe de teste
from utils import Connector 

def cria_conexao():
	con = Connector('banco_de_teste')
	campos_tabela = ['nome varchar(100)', 'idade number(2,0)']

	con.create_table('cliente', campos_tabela)
	print('bla')


cria_conexao()
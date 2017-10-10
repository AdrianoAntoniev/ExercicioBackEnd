## Classe de teste
from utils import Connector 

def cria_conexao():
	con = Connector('banco_de_teste')
	campos_tabela = ['nome varchar(100)', 'idade number(2,0)']

	con.create_table('cliente', campos_tabela)	

def insere_dados(nome, idade):
	sql = 'insert int cliente values(?,?)'		
	con = Connector('banco_de_teste')
	con.insert_into('cliente', (nome, idade))




cria_conexao()
insere_dados('Valmecir almeida', 23)

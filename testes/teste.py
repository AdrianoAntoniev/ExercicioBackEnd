## Classe de teste

import persistencia.utils as utils

def cria_conexao():
	con = utils.Connector('banco_de_teste')
	campos_tabela['nome varchar(100)', 'idade number(2,0)']

	con.create_table('bla', campos_tabela)
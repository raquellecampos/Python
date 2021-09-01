import sqlite3 as conector
from modelo import Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Criação do objeto tipo Pessoa
pessoa = Pessoa(38383838389, 'Silva', '1998-03-30', True)

#Definição de um comando com named paremeter
comando = '''INSERT INTO Pessoa VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''
cursor.execute(comando, vars(pessoa))
print(vars(pessoa))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
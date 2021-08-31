import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(20000000099, 'José','1990-02-28', False)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (:cpf, :nome, :data_nascimento,)'''

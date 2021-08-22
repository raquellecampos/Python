import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
          VALUES (12345678900, 'Raquelle', '1986-05-23', 1);'''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()
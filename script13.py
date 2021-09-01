import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on") #Habilitamos a flag
cursor = conexao.cursor()

# Inserção de dados na tabela Marca
comando1 = '''INSERT INTO Marca(nome, sigla) VALUES (:nome, :sigla);'''

marca1 = Marca("Marca A", "MA")
cursor.execute(comando1, vars(marca1))
marca1.id = cursor.lastrowid #armazena o id da linha do ultimo registro

marca2 = Marca("Marca B", "MB")
cursor.execute(comando1, vars(marca2))
marca2.id = cursor.lastrowid

# Inserção de daos na tabela Veiculo
comando2 = '''INSERT INTO Veiculo
               VALUES(:placa, :ano, :cor, :motor, :proprietario, :marca);'''
veiculo1 = Veiculo("AAA0001", 2001, "Prata", 1.0, 10000080099, marca1.id)
veiculo2 = Veiculo("BAA0002", 2002, "Preto", 1.4, 100000980067, marca1.id)
veiculo3 = Veiculo("CAA0003", 2003, "Branco", 2.0, 200000870659, marca2.id)
veiculo4 = Veiculo("DAA0004", 2004, "Azul", 2.2, 390000607000, marca2.id)
cursor.execute(comando2, vars(veiculo1))
cursor.execute(comando2, vars(veiculo2))
cursor.execute(comando2, vars(veiculo3))
cursor.execute(comando2, vars(veiculo4))


#Como não iremos passar um valor para o id da marca, que é autoincrementado, foi necessário explicitar o nome das
# colunas no comando INSERT INTO. Caso omitíssemos o nome das colunas, seria gerada uma exceção
# do tipo OperationalError, com a descrição indicando que a tabela tem 3 colunas,
# mas apenas dois valores foram fornecidos.
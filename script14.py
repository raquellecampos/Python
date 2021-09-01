import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on") #Checagem da chave estrangeira
cursor = conexao.cursor()

#Definição de comandos
comando1 = '''UPDATE Pessoa SET oculos= 1;'''
cursor.execute(comando1)

comando2 = '''UPDATE Pessoa SET oculos= ? WHERE cpf=300093847576;'''
cursor.execute(comando2, (False,))

comando3 = '''UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;'''
cursor.execute(comando3,{"usa_oculos": False, "cpf": 200093874576})

#Efetivação do comando
conexao.commit()


cursor.close()
conexao.close()
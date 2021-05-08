from pessoa import Pessoa
import sqlite3

#cursor.execute("CREATE TABLE pessoa (nome text, data_nascimento text, idade integer, sexo text, telefone text)")

#  try:
banco = sqlite3.connect('pessoa.db')

cursor = banco.cursor()


cursor.execute("INSERT INTO pessoa VALUES('"+nome+"','"+data_nascimento+"',"+str(idade)+",'"+sexo+"','"+telefone+"')")
#  cursor.execute("DELETE from pessoa WHERE idade = 20")
banco.commit()
#  print("Deu bom")
#  except sqlite3.Error as erro:
#  print("Erro ao excluir",erro)

#  banco.execute("SELECT * FROM pessoa")
#  print(cursor.fetchall())


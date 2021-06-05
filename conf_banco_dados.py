import sqlite3

banco = sqlite3.connect('representante.db')
cursor = banco.cursor()
#   cursor.execute("DELETE from pessoa WHERE sexo = 'Feminino'")
cursor.execute("CREATE TABLE representante (codigo integer, rg integer,nome text, data_nascimento text, sexo text, telefone text, comissao real)")
#  cursor.execute("INSERT INTO pessoa VALUES('634564','Agenaldo','17-06-1978','Masculino','62 9 9744-5834')")
#   cursor.execute("INSERT INTO pessoa VALUES('2','16-06-2021','TF Ubuntu','70','Primeiro')")

banco.commit()

#  cursor.execute("CREATE TABLE evento (id integer primary key, data text,nome text,preco_ingresso real,lote text)")
#  except sqlite3.Error as erro:
#  print("Erro ao excluir",erro)
#  cursor.execute("CREATE TABLE pessoa (nome text, data_nascimento text, idade integer, sexo text, telefone text)")
#
#  cursor.execute("DELETE from pessoa WHERE idade = 20")


#  except sqlite3.Error as erro:
#  print("Erro ao excluir",erro)

#  banco.execute("SELECT * FROM pessoa")
#  print(cursor.fetchall())

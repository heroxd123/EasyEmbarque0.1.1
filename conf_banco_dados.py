from pessoa import Pessoa
import sqlite3

banco = sqlite3.connect('bd_evento')

cursor = banco.cursor()

try:
    cursor.execute("INSERT INTO evento VALUES('1','08-06-2021','Hipnodreams',50,'Promo')")

except:
    print("Erro geral")

#  cursor.execute("CREATE TABLE evento (id integer primary key, data text,nome text,preco_ingresso real,lote text)")
#  except sqlite3.Error as erro:
#  print("Erro ao excluir",erro)
#  cursor.execute("CREATE TABLE pessoa (nome text, data_nascimento text, idade integer, sexo text, telefone text)")
#  cursor.execute("INSERT INTO pessoa VALUES('Agenaldo','17-06-1978',24,'Masculino','62 9 9744-5834')")
#  cursor.execute("INSERT INTO pessoa VALUES('"+nome+"','"+data_nascimento+"',"+str(idade)+",'"+sexo+"','"+telefone+"')")
#  cursor.execute("DELETE from pessoa WHERE idade = 20")


#  except sqlite3.Error as erro:
#  print("Erro ao excluir",erro)

#  banco.execute("SELECT * FROM pessoa")
#  print(cursor.fetchall())


import sqlite3
from sqlite3 import Error

#   Criar Conexão com o banco de dados
def conexao_banco():
    caminho="C:\\EasyEmbarque0.1.1\\evento.db"
    cone=None
    try:
        cone=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return cone

vcon=conexao_banco()

def criar_tabela(conexao,sql):

    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela criado com sucesso, só bora!!!!")

    except Error as ex:
        print(ex)

#   Criar Tabela

vsql="""CREATE TABLE evento(
    id_evento INTEGER PRIMARY KEY AUTOINCREMENT, 
    data VARCHAR(10),
    nome VARCHAR(30),
    preco INTEGER VARCHA;R(6),
    lote VARCHAR(15)    
    );"""

criar_tabela(vcon,vsql)
vcon.close()

def consulta():

    banco = sqlite3.connect('evento.db')
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE evento(id text, data text, nome text, preco integer, lote text)")
    resultado=cursor.fatchall()
    return resultado

vsql="SELECT * pessoa"

#   banco = sqlite3.connect('evento.db')
#   cursor = banco.cursor()
#   cursor.execute("CREATE TABLE evento(id text, data text, nome text, preco integer, lote text)")
#   banco.commit()
#   print("Banco evento criado com sucesso...")

#  cursor.execute("CREATE TABLE evento (id integer primary key, data text,nome text,preco_ingresso real,lote text)")
#  except sqlite3.Error as erro:
#  print("Erro ao excluir",erro)
#  cursor.execute("CREATE TABLE pessoa (nome text, data_nascimento text, idade integer, sexo text, telefone text)")
#
#  cursor.execute("DELETE from pessoa WHERE idade = 20")
#   p=cursor.execute("SELECT * FROM pessoa")
#   print(p)
#   cursor.execute("DELETE from pessoa WHERE sexo = 'Feminino'")

#  except sqlite3.Error as erro:
#  print("Erro ao excluir",erro)
#   cursor.execute("INSERT INTO pessoa VALUES('634564','Agenaldo','17-06-1978','Masculino','62 9 9744-5834')")
#   cursor.execute("INSERT INTO pessoa VALUES('2','16-06-2021','TF Ubuntu','70','Primeiro')")
#  banco.execute("SELECT * FROM pessoa")
#  print(cursor.fetchall())

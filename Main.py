from motorista import Motorista
from pessoa import Pessoa
from evento import Evento

# Criando pessoa(s)
pessoa = Pessoa('634564','Agenaldo','17-06-1978','Masculino','62 9 9744-5834')
pessoa2 = Pessoa("966728","Bationildo", "30/02/1955", "Masculino", "62 9 8712-9801")

# Verificando a idade com o método criado na classe Pessoa


# Criando motorista(s)
motorista = Motorista( '621521', 'paulo', '19/01/2001', 'Masculino', '6291059520', "b",'pedrin dos beck')


# Verificando se a CNH do Motorista é válida
motorista.verificar_cnh()

pessoa.nome = "pedrin dos beck"
print(motorista.nome)
pessoa2.db_regitrar_pessoa()

#Criando evento
evento = Evento("546", '15/03/2022', 'Zuvuya', "90", "segundo")
evento.db_registrar_evento()
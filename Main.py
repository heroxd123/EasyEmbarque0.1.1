from motorista import Motorista
from pessoa import Pessoa

# Criando pessoa(s)
pessoa = Pessoa('634564','Agenaldo','17-06-1978','Masculino','62 9 9744-5834')
pessoa2 = Pessoa("966728","Bationildo", "30/02/1955", "Masculino", "62 9 8712-9801")

# Verificando a idade com o método criado na classe Pessoa


# Criando motorista(s)
motorista = Motorista("A", "Tuezin")
motorista2 = Motorista("B", "Macacão")

# Verificando se a CNH do Motorista é válida
motorista.verificar_cnh()
motorista2.verificar_cnh()

pessoa.db_regitrar_pessoa()

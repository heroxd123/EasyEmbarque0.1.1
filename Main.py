from motorista import Motorista
from pessoa import Pessoa

# Criando pessoa(s)
pessoa = Pessoa("Elisvaldo", "20/11/2000", "Masculino", "62 9 9474-4589")
print(pessoa.nome, pessoa.data_nascimento)

# Criando motorista(s)
motorista = Motorista("A", "Tuezin")
motorista2 = Motorista("B", "Macacão")

# Verificando se a CNH do Motorista é válida
motorista.verificar_cnh()
motorista2.verificar_cnh()

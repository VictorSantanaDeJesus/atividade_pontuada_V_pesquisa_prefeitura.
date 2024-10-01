"""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos das famílias da cidade.
A prefeirtura deseja saber:

a) total de famílias que responderam a pesquisa;
b) média do salário da população;
c) média do número de filhos;
d) maior salário;
e) menor salário.

Crie um menu com as seguintes opções.
Código
1
2
3

Descrição
Adicionar família
Exibir resultados
Sair

Ao adicionar uma família, deve-se limpar o termianl e a apresentar o menu novamente.
1. Salve os dados em um arquivo com o nome: pesquisa_prefeitura.txt
2. O programa deve ler o arquivo para exibir os dados salvos.
"""

import os
from dataclasses import dataclass

os.system("cls || clear")

familias=[]
lista_habitantes = 0
soma_filhos = 0
soma_salario=0

@dataclass
class familia:
    quantidade_filhos: int
    quantidade_salario: float

# Entrada

print("Descrição")

print("1. Adicionar família")
print("2. Exibir resultados")
print("3. Sair")


opcao = input("Escolha uma opção: ")
if opcao == "1":
    salario=float(input("Digite seu salário: "))
    filhos=float(input("Informe o número de filhos: "))

familias.append((salario, filhos))
soma_filhos += salario
soma_salario +=salario

# Estrutura de dados.

with open("pesquisa_prefeitura.txt", "a") as arquivo_habitantes:
    # Percorrendo vetor/lista.
    for habitante in lista_habitantes:
        # Escrevendo no arquivo uma linha de cada vez.
        arquivo_habitantes.write(f"{salario}, {filhos}\n")
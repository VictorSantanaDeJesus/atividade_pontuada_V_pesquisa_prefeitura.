import os
import time
from dataclasses import dataclass

os.system("cls || clear")
def limpa_terminal():
    os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Familia:
    filhos: float
    salario: float

# Lista de de alunos.
lista_de_familias = []
filhos=[]
total_familias = 0
print("\n=== Solicitando dados dos alunos ===")
while True:
    print("Opções do menu:")
    print("\n1. Adicionar família")
    print("2. Exibir resultados")
    print("3. Sair")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
            case 1:
                    lista_salarios = []
                    lista_filhos = []
                    familia = Familia(
                    filhos = int(input("Digite a quantidade de filhos: ")),
                    salario = float(input("Digite o salário da família: "))
                    
                )
                    lista_de_familias.append(familia)
                    total_familias += 1
                    print ("Dados da família salva com sucesso")
                    for familia in lista_de_familias:
                        lista_salarios.append(familia.salario)
                        lista_filhos.append(familia.filhos)
                        media_filhos = sum(lista_filhos) / len(lista_filhos)
                        media_salarios = sum(lista_salarios) / len(lista_salarios)
                        maior_salario = max(lista_salarios)
                        menor_salario = min(lista_salarios)                       

                        limpa_terminal()
            case 2:
                print("\n=== Exibindo resultados ===")  
                print(f"Total de famílias que participaram da pesquisa: {total_familias}")
                print(f"Média de salário da população: {media_salarios}")
                print(f"Média de filhos por família da população: {media_filhos}")
                print(f"Maior salário da população: {maior_salario}")
                print(f"Menor salário da população: {menor_salario}")
                time.sleep (8)
                limpa_terminal()
            case 3: 
                break        
            case _:  
                print("Opção inválida! Tente novamente.")
                time.sleep(1)
                limpa_terminal()


# Definindo arquivo para salvar os dados.
nome_do_arquivo = "pesquisa_prefeitura.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "a") as arquivo_familias:
    # Percorrendo vetor/lista.
    for familia in lista_de_familias:
        # Escrevendo no arquivo uma linha de cada vez.
        arquivo_familias.write(f"{familia.filhos}, {familia.salario}\n")

# Fechar conexão com o arquivo.
arquivo_familias.close()
print("\n=== Dados das famílias salvo com sucesso! ===")


# Lendo dados de um arquivo.
# Limpando a lista de alunos.
lista_de_familias = []

print("\n=== Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        filhos, salario = linha.strip().split(",")
        lista_de_familias.append(Familia(filhos=filhos, salario= float(salario)))

# Fechar conexão com o arquivo.
arquivo_familias.close()


import os
import time
from dataclasses import dataclass

os.system("cls || clear")
def limpa_terminal():
    os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Familia:
    filhos: int
    salario: float



# Lista de de alunos.
lista_de_familias = []

print("\n=== Solicitando dados dos alunos ===")
while True:
print("Opções do menu:")
    print("\n1. Adicionar família")
    print("2. Exibir resultados")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    match opcao:
            case 1:
                    familia = Familia(
                    filhos = int(input("Digite seu nome: ")),
                    salario = float(input("Digite sua idade: "))
                    
                )
                    lista_de_familias.append(familia)
                    print ("Dados da família salva com sucesso")
            case 2:
                for familia in lista_de_familias:
                    print(f"Quantidade de filhos: {familia.filhos}")
                    print(f"Idade: {aluno.idade}")
            case 3: 
                break        
            case _:  
                print("Opção inválida! Tente novamente.")
                time.sleep(1)
                limpa_terminal()

    

print("\n=== Exibindo dados dos alunos ===")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")


# Definindo arquivo para salvar os dados.
nome_do_arquivo = "Lista_de_alunos_SENAI.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "a") as arquivo_alunos:
    # Percorrendo vetor/lista.
    for aluno in lista_de_alunos:
        # Escrevendo no arquivo uma linha de cada vez.
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")

# Fechar conexão com o arquivo.
arquivo_alunos.close()
print("\n=== Dados dos alunos salvo com sucesso! ===")


# Lendo dados de um arquivo.
# Limpando a lista de alunos.
lista_de_alunos = []

print("\n=== Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome, idade = linha.strip().split(",")
        lista_de_alunos.append(Aluno(nome=nome, idade= int(idade)))

# Fechar conexão com o arquivo.
arquivo_alunos.close()

print("\n\n=== Exibindo dados dos alunos do arquivo ===")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
alunos = []

def cadastrar_aluno():

    identificacao = len(alunos) + 1
    print(f"\nDados do aluno {len(alunos) + 1}")    
    nome = input("Digite o nome do aluno : ").strip().title()
    try:    
        idade = int(input("Digite a idade do aluno : "))
    except ValueError:
        print("Digite Apenas a idade aqui.")
        return 
    
    aluno = {
        "nome" : nome,
        "idade" : idade,
        "id" : identificacao,
    }
    alunos.append(aluno)
    return 
        
def listar_alunos():
    contador = 0
    if len(alunos) == 0:
        print("Não há alunos na lista.") 
        return
    for aluno in alunos:  
        contador += 1 
        print()
        print(f"Aluno {contador} ")
        print(f"Nome : ",aluno["nome"])
        print(f"Idade : ",aluno["idade"])
        print(f"Sua identificação é unica : ",aluno["id"])
        print()
    print(f"Total de alunos cadastrados : {len(alunos)}")

def remover_aluno():

    if len(alunos) == 0:
        print("Não há alunos na lista para remover.")
        return
    
    remover_nome = input("Digite o nome e do aluno : ").strip().title()

    for aluno in alunos:
        if aluno["nome"] == remover_nome:
            alunos.remove(aluno)   
            print("Aluno removido, Identificação :", aluno["id"])
            return
    print("Aluno não encontrado." )

def encontrar_aluno():

    if len(alunos) == 0:
            print("Não há alunos na lista.")
            return
    
    buscar_aluno = input("Digite o nome do aluno que você deseja buscar : ").strip().title()
    
    for aluno in alunos:
        if aluno["nome"] == buscar_aluno:
            print("O aluno está na lista")
            print("id do aluno :", aluno["id"])
            return
    print("O aluno não está na lista")

def editar_aluno(): 

    if len(alunos) == 0:
            print("Não há alunos na lista.")
            return
    
    editar_dados = input("Digite o nome do aluno que deseja fazer a edição : ").strip().title()

    for aluno in alunos:

        if editar_dados == aluno["nome"] :
            print("Aluno encontrado.")
            print("\nDados do aluno :")
            print("Nome :", aluno["nome"])
            print("Idade :", aluno["idade"])
            print("Id :", aluno["id"])

            mudar = input("Deseja editar qual dado ? : ").strip().title()
            if mudar == "Nome" :
                mudar_nome = input("Digite o novo nome do aluno : ")
                aluno["nome"] = mudar_nome
                print("Dados do aluno atualizado.")
                return

            elif mudar == "Idade" :
                mudar_idade = int(input("Digite a nova idade do aluno : "))
                aluno["idade"] = mudar_idade
                print("Dados do aluno atualizado.")
                return

            if mudar == "Id" :
                print("Este dado não é possivel de ser alterado, cada aluno tem o seu e é unico.")
                return
    print("Aluno não encontrado, certifique-se que digitou corretamente.")
    return
        

def finalizar_programa():
    print("Obrigado.")
         
def opcao_invalida():
    print("Opção inválida, digite alguma das opções.")

while True:
 
    print("\n1 - Cadastrar alunos")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Buscar aluno")
    print("5 - Editar aluno")
    print("6 - Sair\n")

    try : # Aqui onde eu escolho as opçoes de cadastro
        numero = int(input("Escolha alguma opção : "))
    except ValueError:
        print("Digite Apenas Números Aqui.")
        continue

    if numero == 1:
        cadastrar_aluno()
    
    elif numero == 2:
        listar_alunos()

    elif numero == 3:
        remover_aluno()
    
    elif numero == 4:
        encontrar_aluno()
    
    elif numero == 5:
        editar_aluno()

    elif numero == 6:
        finalizar_programa()
        break

    else:
        opcao_invalida()
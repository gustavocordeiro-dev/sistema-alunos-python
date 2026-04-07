alunos = []

def dados_aluno(aluno): 
        print("Nome :", aluno["nome"])
        print("Idade :", aluno["idade"])
        print("Identificação :", aluno["id"])

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

    if len(alunos) == 0:
        print("Não há alunos na lista.") 
        return
    for aluno in alunos:  
        print(f"\nAluno ", aluno["id"])
        print(f"Nome : ",aluno["nome"])
        print(f"Idade : ",aluno["idade"])
        print(f"Sua identificação é unica : ",aluno["id"])
        print()
    print(f"Total de alunos cadastrados : {len(alunos)}")

def remover_aluno():

    if len(alunos) == 0:
        print("Não há alunos na lista para remover.")
        return
    try:
        remover_nome = int(input("Digite a identificação do aluno : "))
    except ValueError:
        print("Certifique-se de ter digitado os dados corretamente.")
        return

    for aluno in alunos:
        if aluno["id"] == remover_nome:
            print("Aluno removido.")
            print("Dados do aluno :\n")
            dados_aluno()
            alunos.remove(aluno)   
            return
    print("Aluno não encontrado." )

def encontrar_aluno():

    if len(alunos) == 0:
            print("Não há alunos na lista.")
            return
    
    buscar_aluno = int(input("Digite a identificação do aluno que você deseja buscar : "))
    
    for aluno in alunos:
        if aluno["id"] == buscar_aluno:
            print("O aluno está na lista")
            print("Dados do Aluno :\n")
            dados_aluno()
            return
    print("O aluno não está na lista")

def editar_aluno(): 

    if len(alunos) == 0:
            print("Não há alunos na lista.")
            return
    
    try:
        editar_dados = int(input("Digite a identificação do aluno que deseja fazer a edição : "))
    except ValueError:
        print("Certifique-se de ter digitado os dados corretamente.")
        return
    
    for aluno in alunos:

        if editar_dados == aluno["id"] :
            print("Aluno encontrado.")
            print("\nDados do aluno :")
            print("Nome :", aluno["nome"])
            print("Idade :", aluno["idade"])
            print("Identificação :", aluno["id"])

            print("\nDeseja editar : ")
            print("1 - Nome")
            print("2 - Idade\n")

            try:
                mudar = int(input(""))
            except ValueError:
                print("Certifique-se de ter digitado os dados corretamente.")
                return
            
            if mudar == 1 :
                mudar_nome = input("Digite o novo nome do aluno : ")
                aluno["nome"] = mudar_nome
                print("Dados do aluno atualizado.")
                return

            elif mudar == 2 :
                try:
                    mudar_idade = int(input("Digite a nova idade do aluno : "))
                except ValueError:
                    print("Digite apenas números.")
                    return
                aluno["idade"] = mudar_idade
                print("Dados do aluno atualizado.")
                return

    print("Aluno não encontrado, certifique-se que digitou corretamente.")
    return
        

def finalizar_programa():
    print("Obrigado.")
         
def opcao_invalida():
    print("Opção inválida, digite alguma das opções.")

print("\n------SISTEMA CADASTRO DE ALUNOS------\n")
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
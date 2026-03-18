alunos = []

def dados_do_aluno(): #Aqui eu pretendo diminuir mais o código na parte de mostrar os dados

    ...

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
    cont = 0
    if len(alunos) == 0:
        print("Não há alunos para listar.") 
        return
    for aluno in alunos:  
        cont += 1 
        print()
        print(f"Aluno {cont} ")
        print(f"Nome : ",aluno["nome"])
        print(f"Idade : ",aluno["idade"])
        print(f"Sua identificação é unica : ",aluno["id"])
        print()
    print(f"Total de alunos cadastrados : {len(alunos)}")

def remover_aluno():
    remover = input("Digite o nome e do aluno : ").strip().title()
    for aluno in alunos:
        if aluno["nome"] == remover:
            alunos.remove(aluno)   
            print("Aluno removido, id :", aluno["id"])
            return
    print("Aluno não encontrado." )

def encontrar_aluno():
    buscar_aluno = input("Digite o nome do aluno que você deseja buscar : ").strip().title()
    if len(alunos) == 0:
        print("Não há alunos para listar.")
        return
    for aluno in alunos:
        if aluno["nome"] == buscar_aluno:
            print("O aluno está na lista")
            print("id do aluno :", aluno["id"])
            return
    print("O aluno não está na lista")

def editar_aluno(): # Tenho Que Arrumar alguns bugs aqui e melhorar o código.
    edicao = input("Digite o nome do aluno que deseja fazer a edição : ").strip().title()

    for aluno in alunos:
        if edicao == aluno :
            print("Aluno encontrado.")
            print("Dados do aluno :")
            print("Nome :", aluno["nome"])
            print("Idade :", aluno["idade"])
            print("Id :", aluno["id"])

            desejo = input("Deseja editar qual dado? : ").strip().title()
            if desejo == "Nome" :
                edicao_nome = input("Digite o novo nome do aluno : ")
                aluno["nome"] = edicao_nome

            elif desejo == "Idade" :
                edicao_idade = int(input("Digite a nova idade do aluno : "))
                aluno["idade"] = edicao_idade

            if desejo == "Id" :
                print("Este dado não é possivel de ser alterado, cada aluno tem o seu e é unico.")
    
            print("Dados do aluno atualizado.")
            return
        
        print("Este aluno não está cadastrado.")
        

def finalizar_programa():
    print("Obrigado.")
         
def opcao_invalida():
    print("Digite alguma das opçoes")

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
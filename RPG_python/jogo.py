import json

personagens = []


def salvar_dados():
    with open("dados.json", "w", encoding="utf-8") as arq:
        json.dump(personagens, arq,  indent = 6, ensure_ascii= False)

def carregar_dados():
    global personagens
    try:
        with open("dados.json", "r", encoding="utf-8") as arq:
            personagens = json.load(arq)
    except FileNotFoundError:
        personagens = []

def show_menu():
    print("\n========== RPG PYTHON ==========\n")
    print("1 - Criar Personagem")
    print("2 - Listar Personagens")
    print("3 - Pesquisar Personagem")
    print("4 - Ganhar Experiência")
    print("5 - Excluir Personagem")
    print("6 - Sair")


def Criar_personagem():
    nome = input("Digite o nome do seu personagem: ").lower()
    classe = input("Digite a classe do seu personagem: ").lower()
    vida = 100
    ataque = 20
    nivel = 1
    xp = 0
    
    personagem = {
        "nome": nome,
        "classe": classe,
        "vida": vida,
        "ataque": ataque,
        "nivel": nivel,
        "xp": xp
    }
    
    personagens.append(personagem)
    salvar_dados()
    
def listar_personagens():
    for personagem in personagens:
        print(f"Esses são os personagens: \n {personagem['nome'], personagem['classe'], personagem['nivel']}")
        
def pesquisar_personagens():
    nome_personagem = input("Digite o nome do personagem: ").lower()
    encontrado = False
    for personagem in personagens:
        if nome_personagem == personagem['nome']:
            print(f"personagem encontrado!\n {personagem['nome']}")
            encontrado = True
            return
        if encontrado == False:
            print("Personagem não encontrado!")


def ganhar_exp():
    nome_personagem = input("Digite o nome do seu personagem: ").lower()
    encontrado = False
    for personagem in personagens:
        if nome_personagem == personagem['nome']:
            print("Personagem encontrado!")
            encontrado = True
            qtd_xp = int(input("Digite a quantidade de xp obtida( até 100 ): "))
            if qtd_xp <=100:
                personagem['xp'] = qtd_xp
            if personagem['xp'] == 100:
                personagem['nivel'] +=1
            salvar_dados()
    
    if encontrado == False:
        print("Personagem não encontrado!")
        
def excluir_personagem():
    print(personagem['nome'])
    apagar_personagem = input('Escolha qual personagem você quer excluir: ').lower()
    encontrado = False
    for personagem in personagens:
            if apagar_personagem == personagem['nome']:
                print("Personagem encontrado!")
                personagens.remove(personagem)
                encontrado = True
                print("Personagem Excluido com sucesso!")
                break
            salvar_dados()
    if encontrado == False:
        print("Personagem não encontrado! ")
        

def main():
     while True:
        show_menu()
        option = input("escolha uma opção: ")
        
        if option == "1":
            Criar_personagem()
        elif option == "2":
            listar_personagens()
        elif option == "3":
            pesquisar_personagens()
        elif option == "4":
            ganhar_exp()
        elif option == "5":
            excluir_personagem()
        elif option == "6":
            print("Você fechou o banco!")
            break
        else:
            print("opção inválida! tente novamente.")
carregar_dados()
main()
                
                    
    
    
            
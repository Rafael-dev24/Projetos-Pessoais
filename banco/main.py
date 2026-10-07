contas = []

def show_menu():
    print("\n========BANCO========")
    print("1 - criar conta")
    print("2 - ver contas")
    print("3 - depositar")
    print("4 - sacar")
    print("5 - consultar saldo")
    print("6 - sair")

def criar_conta():
    numero = int(input("digite o seu número: "))
    nome = input("Digite seu nome: ").lower()
    idade = int(input("Digite sua idade: "))
    saldo = 0
    
    conta = {
        
    "numero": numero,
    "nome": nome,
    "idade": idade,
    "saldo": saldo
    
    }
    contas.append(conta)

def ver_contas():
    for conta in contas:
        print(f"Número: {conta['numero']}")
        print(f"Olá {conta['nome']}")
        print(f"Idade: {conta['idade']}")
        print(f"seu saldo: {conta['saldo']}")
        
def depositar_saldo():
    numero_conta = int(input("Digite o número da sua conta:"))
    depositar = float(input("deposite seu saldo: "))
    
    encontrado = False
    
    for conta in contas:
        if numero_conta == conta['numero']:
            conta['saldo'] += depositar
            encontrado = True
    if encontrado == False:
        print("Essa conta não existe!")    
            

def sacar():
    numero_conta = int(input("Digite o número da conta: "))
    saque = float(input("Digite o valor de saque: "))
    encontrado = False
    
    for conta in contas:
        if numero_conta == conta['numero']:
            encontrado = True
            if saque <= conta['saldo']:
                conta['saldo'] -= saque
    if encontrado == False:
        print("essa conta não existe!")

def consultar_saldo():
    numero_conta = int(input("Digite o número da conta: "))
    
    for conta in contas:
        if numero_conta == conta['numero']:
            print(f"Seu saldo é de: {conta['saldo']}")

def main():
    while True:
        show_menu()
        option = input("escolha uma opção: ")
        
        if option == "1":
            criar_conta()
        elif option == "2":
            ver_contas()
        elif option == "3":
            depositar_saldo()
        elif option == "4":
            sacar()
        elif option == "5":
            consultar_saldo()
        elif option == "6":
            print("Você fechou o banco!")
            break
        else:
            print("opção inválida! tente novamente.")

main()

         
        
        
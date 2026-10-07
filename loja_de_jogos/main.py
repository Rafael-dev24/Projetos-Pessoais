jogos = []

def show_menu():
    print("\n=== LOJA DE JOGOS ===")
    print("1 - Cadastrar jogo")
    print("2 - Listar jogo")
    print("3 - Pesquisar jogo")
    print("4 - Calcular valor total")
    print("5 - jogos em promoção")
    print("6 - Sair")
    

def cadastrar_jogo():
    code = input("código do jogo: ")
    nome = input("Digite o nome do jogo: ")
    preco = float(input("Digite o preço do jogo: "))
    ano_lancamento = input("Digite o ano de lançamento: ")
    promocao = input("Está em promoção?: ").lower()
    
    jogo = {
    "código": code,
    "nome": nome, 
    "preço": preco,
    "ano_lancamento": ano_lancamento,
    "promoção": promocao
    }
    
    jogos.append(jogo)
    
def listar_jogos():
    for jogo in jogos:
        print(jogo["código"] , jogo["nome"], jogo["preço"], jogo["ano_lancamento"], jogo["promoção"])
        
def pesquisar_jogo():
    pesquisa = input("digite o nome do jogo: ").lower()
    
    encontrado = False
    
    for jogo in jogos:
        if pesquisa == jogo["nome"]:
            print(jogo["nome"])
            encontrado = True
    if encontrado == False:
        print("Jogo não encontrado!")

def valor_total():
    valor_total = 0 
    
    for jogo in jogos:
        valor_total += jogo["preço"]
        print(f"o valor de todos os jogos é de: {valor_total}")
        
def ver_promocao():
    for jogo in jogos:
        if jogo["promoção"] == "sim":
            print("promoção para esse jogo é de 25% ")
        else:
            print("então continue comprando! ")

def main():
    while True:
        show_menu()
        option = input("escolha uma opção: ")
        
        if option == "1":
            cadastrar_jogo()
        elif option == "2":
            listar_jogos()
        elif option == "3":
            pesquisar_jogo()
        elif option == "4":
            valor_total()
        elif option == "5":
            ver_promocao()
        elif option == "6":
            print("sistema encerrado!")
            break
        else:
            print("opção inválida!")
        
main()
        
     
    
import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaCarros as mcar
import apresentacao as apresentacao


def main():
    opcao = apresentacao.MenuPrincipal()
    while opcao != 9:
        if opcao == 1:
            print("Locações")
        elif opcao == 2:
            print("Clientes")
        elif opcao == 3:
            print("Carros")
        else:
            print("Opção inválida")
        opcao = apresentacao.MenuPrincipal()
    ###
    print("*"*30)
    print("Exemplo de carregamento de dados de um arquivo csv")
    listaClientes = mcli.carregar()
    print(listaClientes)
    print("*"*30)
    print()
    print("*"*30)
    print("Exemplo de leitura dos campos e armazenamento em um arquivo csv")
    mcli.cadastrar(listaClientes)
    print("*"*30)
    print()
    print("*"*30)
    print("Exemplo de exclusão de um cliente e armazenamento em um arquivo csv")
    cpf = input("Qual cpf do cliente que deseja excluir? ")
    if  mcli.excluir(listaClientes, cpf) == True:
        print("Cliente excluido com sucesso")
    else:
        print("Cliente não encontrado")
    print()
    print("*"*30)
    print("Exemplo de leitura dos campos e armazenamento em um arquivo csv")
    print("*"*30)
    listaCarros = mcar.carregar()
    mcar.cadastrar(listaCarros)
    

# Inicio do programa 
if __name__ == "__main__":
    main()
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
            opcao2 = apresentacao.MenuClientes()
            while opcao2 != 9:
                if opcao2 == 1:
                    mcli.cadastrar(mcli.carregar())
                elif opcao2 == 2:
                    cpf = input("Qual cpf do cliente que deseja excluir? ")
                    if  mcli.excluir(mcli.carregar(), cpf) == True:
                        print("Cliente excluido com sucesso")
                    else:
                        print("Cliente não encontrado")
                elif opcao2 == 3:
                    apresentacao.listar(mcli.carregar())
                elif opcao2 == 4:
                    cpf = input("Qual cpf do cliente que deseja alterar? ")
                    cliente = mcli.busca1Cliente(mcli.carregar(), cpf)
                    for campo in cliente.keys():
                        print(campo, ":", cliente[campo], "deseja alterar? (s/n)")
                        if input() == 's':
                            cliente[campo] = input("Novo valor: ")
                    mcli.atualizar(mcli.carregar(), cliente)
                else:
                    print("Opção inválida")
                opcao2 = apresentacao.MenuClientes()
        elif opcao == 3:
            opcao3 = apresentacao.MenuCarros()
            while opcao3 != 9:
                if opcao3 == 1:
                    mcar.cadastrar(mcar.carregar())
                elif opcao3 == 2:
                    placa = input("Qual placa do carro que deseja excluir? ")
                    if  mcar.excluir(mcar.carregar(), placa) == True:
                        print("Carro excluido com sucesso")
                    else:
                        print("Carro não encontrado")
                elif opcao3 == 3:
                    apresentacao.listar(mcar.carrergarCarrosDisponiveis())
                else:
                    print("Opção inválida")
                opcao3 = apresentacao.MenuCarros()
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
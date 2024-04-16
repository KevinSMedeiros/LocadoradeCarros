import manipulaClientes as mcli
import manipulaCarros as mcar
import manipulaLocacoes as mloc
import apresentacao as apresentacao


def main():
    opcao = apresentacao.MenuPrincipal()

    while opcao != 9:

        if opcao == 1:
            opcao1 = apresentacao.MenuLocacao()

            while opcao1 != 9:

                if opcao1 == 1:  # cadastrar nova locação
                    if mloc.cadastrar(mloc.carregar()):
                        print("\nLocação registrada com sucesso\n")
                        break
                    else:
                        break

                elif opcao1 == 2:  # finalizar locação
                    if mloc.encerrar():
                        print("\nLocação finalizada com sucesso\n")
                        break
                    else:
                        print("\nLocação não finalizada\n")
                        break

                elif opcao1 == 3:  # relatório de carros locados
                    mcar.mostraCarrosLocados()
                    break

                else:
                    print("Opção inválida")

        elif opcao == 2:
            opcao2 = apresentacao.MenuClientes()

            while opcao2 != 9:

                if opcao2 == 1:  # cadastrar novo cliente
                    mcli.cadastrar(mcli.carregar())

                elif opcao2 == 2:  # excluir cliente
                    cpf = input("Qual cpf do cliente que deseja excluir? ")
                    if mcli.excluir(mcli.carregar(), cpf) == True:
                        print("Cliente excluido com sucesso")
                    else:
                        print("Cliente não encontrado")

                elif opcao2 == 3: # localizar locações do cliente
                    mcli.locacoesDoCliente()

                elif opcao2 == 4:  # alterar informações do cliente
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

                if opcao3 == 1:  # cadastrar novo carro
                    mcar.cadastrar(mcar.carregar())

                elif opcao3 == 2:  # excluir carro
                    placa = input("Qual placa do carro que deseja excluir? ")
                    if  mcar.excluir(mcar.carregar(), placa) == True:
                        print("Carro excluido com sucesso")
                    else:
                        print("Carro não encontrado")

                elif opcao3 == 3:  # listar carros
                    apresentacao.listar(mcar.carrergarCarrosDisponiveis())

                elif opcao3 == 4:
                    apresentacao.listar(mcar.carro3OuMaisAnosOu60kkm(mcar.carregar()))

                elif opcao3 == 5:  # listar carros por categoria
                    categoria = input("Qual categoria deseja buscar? opções: Economico, Intermediario, Conforto, Pickup")
                    apresentacao.listar(mcar.buscaCarroPorCategoria(mcar.carregar(), categoria))

                else:
                    print("Opção inválida")

                opcao3 = apresentacao.MenuCarros()
        else:
            print("Opção inválida")

        opcao = apresentacao.MenuPrincipal()   

# Inicio do programa 
if __name__ == "__main__":
    main()

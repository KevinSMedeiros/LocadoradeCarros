import manipulaCSV as mcsv
import manipulaCarros as mcar
import apresentacao


def carregar() -> list:
    lista = mcsv.carregarDados("Locacao.csv")
    #print(lista)
    return lista


def cadastrar( listaLocacoes : list ) -> bool :

    l = ["IdLocacao", "IdCarro", "CPF", "DataInicio", "DataDevolucao", "KmInicial", "KmFinal", "QuerSeguro", "ValorTotal"]

    # enumera as possiveis opcoes de pesquisa de carros
    Categoria_opcoes = ["Economico", "Intermediario", "Conforto", "Pickup"]
    Cambio_opcoes = ["manual", "automático"]
    Bool_opcoes = ["True", "False"]

    CategoriaCarro = ""
    CambioCarro = ""
    QuerSeguro = ""

    print("\n######## NOVA LOCAÇÃO ########")

    IdLocacao = mcsv.pegaProximoId("Locacao.csv")

    CPF = input("\nDigite o CPF: ")

    print(f"\nCategoria do carro que deseja: {Categoria_opcoes}")
    while CategoriaCarro not in Categoria_opcoes:
        CategoriaCarro = input(f"{"Categoria"}:")

    print(f"\nTipo de câmbio que deseja: {Cambio_opcoes}")
    while CambioCarro not in Cambio_opcoes:
        CambioCarro = input(f"{"Cambio"}:")

    print(f"\nQuer seguro? {Bool_opcoes}")
    while QuerSeguro not in Bool_opcoes:
        QuerSeguro = input(f"{"Seguro"}:")

    DataInicio = input("\nDigite a data e hora atual (Formato DD/MM/AAAA XXh): ")

    listaCarros = mcar.carrergarCarrosDisponiveis()

    achou = -1
    # varre todos os carros em busca de algum com todas as características desejadas
    for carro in listaCarros:
        print(f"Modelo: {carro["Modelo"]}")
        if carro["Categoria"] == CategoriaCarro and carro["Cambio"] == CambioCarro:

            print("\nCarro encontrado:\n")
            print(f"Modelo: {carro["Modelo"]}")
            print(f"Cor: {carro["Cor"]}")
            print(f"Preço da Diária: R${carro["Diaria"]}")
            if QuerSeguro == "True":
                print(f"Preço do Seguro: {carro["Seguro"]}")
            print(f"Quilometragem Atual: {carro["Km"]}")
            print(f"Placa do Carro: {carro["Placa"]}")

            # opção pra aceitar ou não o carro. se rejeitar, procura outro
            AceitaCarro = ""
            print(f"\nAceita esse carro? {Bool_opcoes}")
            while AceitaCarro not in Bool_opcoes:
                AceitaCarro = input("Opções: ")
            if AceitaCarro == "True":
                achou = 1
                break

    if achou == 1:  # se conseguiu encontrar algum carro com as características desejadas
        IdCarro = carro["Identificacao"]
        KmInicial = carro["Km"]

        locacao = apresentacao.CadastrarLocacao(IdLocacao, IdCarro, CPF, DataInicio, KmInicial, QuerSeguro)
        listaLocacoes.append(locacao)

        carro["Disponivel"] = False  # marca que o carro ficou indisponível
        mcar.atualizar(mcar.carregar(), carro)

        return mcsv.gravarDados('Locacao.csv', list(locacao.keys()), listaLocacoes)

    else:  # se nao existir nenhum carro nas caracteristicas desejadas, ou se rejeitou todos que foram oferecidos
        print("\nNão há carro disponível com essas características\n")
        return False



def encerrar( listaLocacoes : list ) -> bool :

    idLocacao = input("\nDigite o id da locação: ")
    dataLocacao = input("\nDigite a data e hora da devolução: ")
    kmLocacao = input("\nDigite a quilometragem do carro no momento da entrega: ")

    locacao = mcsv.retornaNaLinha("Locacao.csv", int(idLocacao) - 1)
    #print(f"AQUI ESTA {locacao}")
    locacao = apresentacao.EncerrarLocacao(locacao, dataLocacao, kmLocacao, idLocacao)

    if atualizar(carregar(), locacao):

        carro = mcar.buscaCarroPorId(mcar.carregar(), locacao["IdCarro"])

        carro["Disponivel"] = True  # marca que o carro ficou disponível
        if mcar.atualizar(mcar.carregar(), carro):
            return True
        else:
            print("Erro ao atualizar carro")
            return False
    else:
        print("Erro ao atualizar locacao")
        return False


def atualizar(listaLocacoes: list, locacao: dict) -> bool:

    flag = False
    camposLocacao = list(["IdLocacao", "IdCarro", "CPF", "DataInicio", "DataDevolucao", "KmInicial", "KmFinal", "QuerSeguro", "ValorTotal"])

    for i, existeLocacao in enumerate(listaLocacoes):
        # aux = mcsv.retornaNaLinha("Locacao.csv", i)

        #if aux["IdLocacao"] == locacao["IdLocacao"]:
        if existeLocacao["IdLocacao"] == locacao["IdLocacao"]:
            flag = True
            listaLocacoes[i] = locacao
    if flag:
        mcsv.gravarDados("Locacao.csv", camposLocacao, listaLocacoes)
    return flag


def busca1Locacao(listaLocacoes : list, idLocacao : int) -> list:
    '''
    Busca um cliente na lista de clientes
    Parâmetros
    ----------
    listaClientes: Lista atual dos clientes
    cpf: cpf do cliente a ser buscado
    Retorno
    -------
    Retorna um dicionário com os dados do cliente
    '''
    for locacao in listaLocacoes:
        if locacao["IdLocacao"] == idLocacao:
            return locacao
    return None

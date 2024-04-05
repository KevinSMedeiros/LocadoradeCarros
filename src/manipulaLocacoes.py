import manipulaCSV as mcsv
import manipulaCarros as mcar
import apresentacao
import datetime
import math


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

        DiaMesAno = input("\nDigite a data atual (Formato DD/MM/AAAA): ")
        HoraMinuto = input("\nDigite o horário atual (Formato HH:MM): ")

        DataInicio = DiaMesAno + " " + HoraMinuto

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
    locacao = mcsv.retornaNaLinha("Locacao.csv", int(idLocacao) - 1)
    Dia = locacao["DataDevolucao"]

    while Dia != "00/00/0000 00:00":
        idLocacao = input("\nEssa locação já foi finalizada. Digite outro id: ")
        locacao = mcsv.retornaNaLinha("Locacao.csv", int(idLocacao) - 1)
        Dia = locacao["DataDevolucao"]


    kmLocacao = input("\nDigite a quilometragem do carro no momento da entrega: ")

    DiaMesAno = input("\nDigite a data da devolução (Formato DD/MM/AAAA): ")
    HoraMinuto = input("\nDigite o horário da devolução (Formato HH:MM): ")

    dataLocacao = DiaMesAno + " " + HoraMinuto
    # dataLocacao = formataData(DiaMesAno, HoraMinuto)


    #print(f"AQUI ESTA {locacao}")
    locacao = apresentacao.EncerrarLocacao(locacao, dataLocacao, kmLocacao, idLocacao)

    valorTotal = calculaValorTotal(locacao)
    locacao["ValorTotal"] = valorTotal


    if atualizar(carregar(), locacao):

        carro = mcar.buscaCarroPorId(mcar.carregar(), locacao["IdCarro"])
        carro["Km"] = locacao["KmFinal"]
        carro["Disponivel"] = True  # marca que o carro ficou disponível
        if mcar.atualizar(mcar.carregar(), carro):
            print(f"\nValor total da locação: R${valorTotal}")
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


def puxaDiaMesAno(horario):

    dataAux = datetime.datetime.strptime(horario, "%d/%m/%Y %H:%M")

    data = dataAux.strftime("%d/%m/%Y")

    return data

def puxaHorario(horario):
    # Convertendo a string para um objeto datetime
    horarioAux = datetime.datetime.strptime(horario, "%d/%m/%Y %H:%M")

    # Formatando a data no novo formato
    horario = horarioAux.strftime("%H:%M")

    return horario

def formataData(data, horario):
    # (DD/MM/AAAA) (HH:MM)
    data = data + " " + horario
    dataAux = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")

    return dataAux

def contaTempo(data1: datetime.datetime, data2: datetime.datetime):
    tempo_decorrido = data2 - data1
    # print(tempo_decorrido)
    if (tempo_decorrido.days > 0):
        [dummy, horas] = str(tempo_decorrido).split(',')
        [horas, minutos, segundos] = horas.split(":")
    else:
        [horas, minutos, segundos] = str(tempo_decorrido).split(":")

    dias = tempo_decorrido.days
    hrs = math.trunc(tempo_decorrido.seconds/3600)

    #print(f"{dias} dias e {hrs} horas utilizadas")

    tempo = {"dias": dias, "horas": hrs}

    return tempo

def calculaValorTotal(locacao) -> float:
    # pega a data inicial e final, conta a diferenca de tempo
    # a cada 24h cobra uma diária, horas restantes são consideradas frações

    carroLocado = mcar.buscaCarroPorId(mcar.carregar(), locacao["IdCarro"])
    print(carroLocado)
    precoDiaria = float(carroLocado["Diaria"])


    if locacao["QuerSeguro"] == "True":
        precoSeguro = float(carroLocado["Seguro"])
    else:
        precoSeguro = 0


    data1 = formataData(puxaDiaMesAno(locacao["DataInicio"]), puxaHorario(locacao["DataInicio"]))
    data2 = formataData(puxaDiaMesAno(locacao["DataDevolucao"]), puxaHorario(locacao["DataDevolucao"]))

    tempo = contaTempo(data1, data2)

    if tempo["dias"] >= 1:
        valorTotal = (precoDiaria + precoSeguro) * (tempo["dias"] + tempo["horas"]/24)
    else:
        valorTotal = precoDiaria + precoSeguro

    return valorTotal


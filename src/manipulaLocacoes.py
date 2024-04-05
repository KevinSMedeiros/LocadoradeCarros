import manipulaCSV as mcsv
import manipulaCarros as mcar
import apresentacao
import datetime
import math


def carregar() -> list:  # chama função para puxar as informações do arquivo como uma lista
    lista = mcsv.carregarDados("Locacao.csv") 
    #print(lista)
    return lista


def cadastrar( listaLocacoes : list ) -> bool :  # adicionar nova locação

    l = ["IdLocacao", "IdCarro", "CPF", "DataInicio", "DataDevolucao", "KmInicial", "KmFinal", "QuerSeguro", "ValorTotal"]

    # enumera as possiveis opcoes de pesquisa de carros
    Categoria_opcoes = ["Economico", "Intermediario", "Conforto", "Pickup"]
    Cambio_opcoes = ["manual", "automático"]
    Bool_opcoes = ["True", "False"]

    CategoriaCarro = ""
    CambioCarro = ""
    QuerSeguro = ""

    print("\n######## NOVA LOCAÇÃO ########")

    IdLocacao = mcsv.pegaProximoId("Locacao.csv")  # o id é igual ao id anterior + 1

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
            # se a categoria e o cambio for igual aos que o usuario quer
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

        DataInicio = DiaMesAno + " " + HoraMinuto  # junta dia e hora na mesma string

        locacao = apresentacao.CadastrarLocacao(IdLocacao, IdCarro, CPF, DataInicio, KmInicial, QuerSeguro)
        listaLocacoes.append(locacao)

        carro["Disponivel"] = False  # marca que o carro ficou indisponível
        mcar.atualizar(mcar.carregar(), carro)

        return mcsv.gravarDados('Locacao.csv', list(locacao.keys()), listaLocacoes)  # chama função pra salvar a nova locação

    else:  # se nao existir nenhum carro nas caracteristicas desejadas, ou se rejeitou todos que foram oferecidos
        print("\nNão há carro disponível com essas características\n")
        return False



def encerrar( listaLocacoes : list ) -> bool :  # função para marcar locação como finalizada

    idLocacao = input("\nDigite o id da locação: ")
    locacao = mcsv.retornaNaLinha("Locacao.csv", int(idLocacao) - 1)  # puxa as informações da locação com o id digitado
    Dia = locacao["DataDevolucao"]

    while Dia != "00/00/0000 00:00":
        # se a data de devolucao não for só zeros, significa que a locação já foi encerrada
        # o id de outra locação vai ser pedido
        idLocacao = input("\nEssa locação já foi finalizada. Digite outro id: ")
        locacao = mcsv.retornaNaLinha("Locacao.csv", int(idLocacao) - 1)
        Dia = locacao["DataDevolucao"]


    kmLocacao = input("\nDigite a quilometragem do carro no momento da entrega: ")

    DiaMesAno = input("\nDigite a data da devolução (Formato DD/MM/AAAA): ")
    HoraMinuto = input("\nDigite o horário da devolução (Formato HH:MM): ")

    dataLocacao = DiaMesAno + " " + HoraMinuto  # junta o dia e a hora na mesma string
    # dataLocacao = formataData(DiaMesAno, HoraMinuto)


    #print(f"AQUI ESTA {locacao}")
    locacao = apresentacao.EncerrarLocacao(locacao, dataLocacao, kmLocacao, idLocacao)

    valorTotal = calculaValorTotal(locacao)  # função pra calcular o valor final
    locacao["ValorTotal"] = valorTotal


    if atualizar(carregar(), locacao): # se conseguiu atualizar

        carro = mcar.buscaCarroPorId(mcar.carregar(), locacao["IdCarro"])
        carro["Km"] = locacao["KmFinal"]
        carro["Disponivel"] = True  # marca que o carro ficou disponível
        
        if mcar.atualizar(mcar.carregar(), carro):  # se conseguiu atualizar o carro
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

    # procura por uma locação com o id definido
    for i, existeLocacao in enumerate(listaLocacoes):
        if existeLocacao["IdLocacao"] == locacao["IdLocacao"]:  
            flag = True
            listaLocacoes[i] = locacao
            
    if flag:  # se achou, então grava na linha certa
        mcsv.gravarDados("Locacao.csv", camposLocacao, listaLocacoes)
        
    return flag


########################################################


def formataData(data, horario):
    # (DD/MM/AAAA) (HH:MM)
    data = data + " " + horario  # pega o dia e o horario e junta na mesma string
    dataAux = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")

    return dataAux

def puxaDiaMesAno(horario):
    # função pega string no formato "DD/MM/AAAA HH:MM"
    dataAux = datetime.datetime.strptime(horario, "%d/%m/%Y %H:%M")
    
    # Devolve só "DD/MM/AAAA"
    data = dataAux.strftime("%d/%m/%Y")

    return data

def puxaHorario(horario):
    # função pega string no formato "DD/MM/AAAA HH:MM"
    
    horarioAux = datetime.datetime.strptime(horario, "%d/%m/%Y %H:%M")

    # Devolve só "HH:MM"
    horario = horarioAux.strftime("%H:%M")

    return horario


def contaTempo(data1: datetime.datetime, data2: datetime.datetime):
    tempo_decorrido = data2 - data1  # calcula a diferença de tempo entre a data de inicio e a data final
    
    if (tempo_decorrido.days > 0):
        [dummy, horas] = str(tempo_decorrido).split(',')
        [horas, minutos, segundos] = horas.split(":")
    else:
        [horas, minutos, segundos] = str(tempo_decorrido).split(":")

    dias = tempo_decorrido.days
    hrs = math.trunc(tempo_decorrido.seconds/3600)

    tempo = {"dias": dias, "horas": hrs}  # dicionario com campos separados pra dia e horario

    return tempo

########################################################

def calculaValorTotal(locacao) -> float:

    carroLocado = mcar.buscaCarroPorId(mcar.carregar(), locacao["IdCarro"])  # puxa dados do carro
    precoDiaria = float(carroLocado["Diaria"]) 


    if locacao["QuerSeguro"] == "True":  # se quer seguro, o preço é adicionado
        precoSeguro = float(carroLocado["Seguro"])
    else:  # se não, fica 0
        precoSeguro = 0

    #  pega as datas de inicio e devolução no formato certo
    data1 = formataData(puxaDiaMesAno(locacao["DataInicio"]), puxaHorario(locacao["DataInicio"]))
    data2 = formataData(puxaDiaMesAno(locacao["DataDevolucao"]), puxaHorario(locacao["DataDevolucao"]))

    tempo = contaTempo(data1, data2)  # calcula o tempo que carro ficou com o cliente

    if tempo["dias"] >= 1:  #  se diaria foi mais que 24 horas
        valorTotal = (precoDiaria + precoSeguro) * (tempo["dias"] + tempo["horas"]/24)
    else:  # se foi menos que 24 horas, cliente paga diaria completa
        valorTotal = precoDiaria + precoSeguro

    return valorTotal


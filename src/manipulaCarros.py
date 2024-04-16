import manipulaCSV as mcsv
import manipulaLocacoes as mloc
import manipulaClientes as mcli
import apresentacao
from datetime import datetime


def carregar() -> list :
    '''
    Carrega o arquivo de Carro.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("Carro.csv")
    return lista
def carrergarCarrosDisponiveis() -> list:
    '''
    Carrega o arquivo de Carro.csv numa lista
    Retorna uma lista de carros disponíveis
    '''
    listaCarros = carregar()
    listaCarrosDisponiveis = []
    for carro in listaCarros:
        if carro['Disponivel'] == 'True':
            listaCarrosDisponiveis.append(carro)
    return listaCarrosDisponiveis

def cadastrar( listaCarros : list) -> bool :
    '''
    Rotina para cadastrar um carro

    Parâmetros
    ----------
    listaClientes: Lista atual dos carros

    Retorno
    -------
    Retorna True se o carro foi cadastrado com sucesso
    '''
    identificacao = mcsv.pegaProximoId("Carro.csv")
    carro = apresentacao.CadastrarCarro(identificacao)
    #averigua se há carro com tal placa
    if not any(c['Placa'] == carro['Placa'] for c in listaCarros):
        listaCarros.append(carro)
        print(listaCarros)
        return mcsv.gravarDados('Carro.csv', carro.keys(), listaCarros )  # Add the missing colon
    else:
        print("Placa já cadastrada")
        return False
def excluir(listaCarros : list, placa : str ) -> bool:
    '''
    Excluir um carro da lista de carros e atualiza o arquivo CSV
    '''
    flag = False
    camposCarro = list(listaCarros[0].keys())
    for i,carro in enumerate(listaCarros):
        if carro['Placa'] ==  placa :
            flag = True
            listaCarros.pop(i)

    if flag:
        mcsv.gravarDados("Carro.csv", camposCarro, listaCarros)
    return flag
def atualizar(listaCarros : list, carro : dict) -> bool:
    '''
    Atualiza um carro na lista de carros e atualiza o arquivo CSV
    Parâmetros
    ----------
    listaCarros: Lista atual dos carros
    carro: Dicionário contendo os dados do carro a ser atualizado
    Retorno
    -------
    Retorna True se o carro foi atualizado com sucesso
    '''
    flag = False
    camposCarro = list(listaCarros[0].keys())
    for i,car  in enumerate(listaCarros):
        if car['Placa'] ==  carro['Placa'] :
            flag = True
            listaCarros[i] = carro
    if flag:
        mcsv.gravarDados("Carro.csv", camposCarro, listaCarros)
    return flag
def buscaCarroPorCategoria(listaCarros: list, categoria: str) -> list:
    '''
    Busca carros na lista de carros pela categoria

    Parâmetros
    ----------
    listaCarros: Lista atual dos carros
    categoria: String contendo a categoria do carro a ser buscado
    Retorno
    -------
    Retorna uma lista de carros se encontrado, None caso contrário
    '''
    listaCarrosCategoria = []
    for carro in listaCarros:
        if carro['Categoria'] == categoria:
            listaCarrosCategoria.append(carro)
    return listaCarrosCategoria
def carro3OuMaisAnosOu60kkm(listaCarros: list) -> list:
    '''
    Busca carros na lista de carros com 3 ou mais anos ou 60000 km

    Parâmetros
    ----------
    listaCarros: Lista atual dos carros
    Retorno
    -------
    Retorna uma lista de carros se encontrado, None caso contrário
    '''
    listaCarros3OuMaisAnosOu60kkm = []
    for carro in listaCarros:
        if (int(carro['AnoFabricacao']) < datetime.now().year - 3 or int(carro['Km']) >= 60000) and carro['Disponivel'] == 'True':
            listaCarros3OuMaisAnosOu60kkm.append(carro)
    return listaCarros3OuMaisAnosOu60kkm
def busca1carro(listaCarros: list, placa: str) -> dict:
    '''
    Busca um carro na lista de carros pelo número da placa

    Parâmetros
    ----------
    listaCarros: Lista atual dos carros
    placa: String contendo a placa do carro a ser buscado
     Retorno
        -------
    Retorna o carro se encontrado, None caso contrário
    '''
    for carro in listaCarros:
         if carro['Placa'] == placa:
             return carro
    return None

def buscaCarroPorId(listaCarros: list, identificacao: int) -> dict:
    '''
    Busca um carro na lista de carros pelo número da placa

    Parâmetros
    ----------
    listaCarros: Lista atual dos carros
    placa: String contendo a placa do carro a ser buscado
     Retorno
        -------
    Retorna o carro se encontrado, None caso contrário
    '''
    for carro in listaCarros:
        if carro["Identificacao"] == identificacao:
            return carro
    return None


def mostraCarrosLocados() -> bool:
    '''
        Varre todas as locações em busca daquelas que ainda estão em andamento
        Quando encontra alguma, o algoritmo puxa todas as informações relacionadas dos outros arquivos

        No final, o valor total é calculado com base na data atual e as informações são printadas
    '''

    print("\n#### RELATÓRIO DE CARROS LOCADOS ####\n")

    listaCarros = carregar()
    listaLocacoes = mloc.carregar()
    listaClientes = mcli.carregar()

    valorAReceber = 0

    ##print(listaLocacoes)

    DiaMesAno = input("\nDigite a data atual (Formato DD/MM/AAAA): ")
    HoraMinuto = input("Digite o horário atual (Formato HH:MM): ")

    DataFinal = mloc.formataData(DiaMesAno, HoraMinuto)

    for i in range(len(listaLocacoes)):
        locacao = mcsv.retornaNaLinha("Locacao.csv", i)  # puxa as informações da locação com o id digitado
        #print(locacao)
        Dia = locacao["DataDevolucao"]
        #print(Dia)

        if Dia == "00/00/0000 00:00":
            # se a data de devolução  for só zeros, significa que a locação ainda está em andamento

            CPF = locacao["CPF"]

            carro = buscaCarroPorId(listaCarros, locacao["IdCarro"])
            cliente = mcli.busca1Cliente(listaClientes, CPF)
            if cliente is None:
                print("Erro ao carregar o cliente")


            nome = cliente["Nome"]
            inicioLocacao = locacao["DataInicio"]
            modelo = carro["Modelo"]
            categoria = carro["Categoria"]
            placa = carro["Placa"]

            valorAReceber = valorAReceber + mloc.calculaValorTotal(locacao, DataFinal)
            valorAReceber = round(valorAReceber, 2)

            print(f"\nCARRO {carro["Identificacao"]}: ")
            print(f"CPF do Cliente: {CPF}")
            print(f"Nome do Cliente: {nome}")
            print(f"Início da Locação: {inicioLocacao}")
            print(f"Modelo do Carro: {modelo}")
            print(f"Categoria do Carro: {categoria}")
            print(f"Placa do Carro: {placa}")

    print(f"\nValor total a receber até o momento: R${valorAReceber}\n")
    return True

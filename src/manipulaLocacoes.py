import manipulaCSV as mcsv
import manipulaCarros as mcar
import apresentacao


def carregar() -> list:
    lista = mcsv.carregarDados("Locacao.csv")
    return lista
    

def cadastrar( listaLocacoes : list ) -> bool :

    Categoria_opcoes = ["Economico", "Intermediario", "Conforto", "Pickup"]
    Cambio_opcoes = ["manual", "automático"]
    Seguro_opcoes = ["True", "False"]

    CategoriaCarro = ""
    CambioCarro = ""
    SeguroOpcao = ""

    CPF = input("Digite o CPF: ")

    print(f"Categoria do carro que deseja: {Categoria_opcoes}")
    while CategoriaCarro not in Categoria_opcoes:
        CategoriaCarro = input(f"{"Categoria"}:")

    print(f"Tipo de câmbio que deseja: {Cambio_opcoes}")
    while CambioCarro not in Cambio_opcoes:
        CambioCarro = input(f"{"Cambio"}:")

    print(f"Quer seguro? {Seguro_opcoes}")
    while SeguroOpcao not in Seguro_opcoes:
        SeguroOpcao = input(f"{"Seguro"}:")

    #l = ["Identificacao", "Modelo", "Cor", "AnoFabricacao", "Placa", "Cambio", "Categoria", "Km", "Diaria", "Seguro",
    #     "Disponivel"]
    #carro = {}

    listaCarros = mcar.carrergarCarrosDisponiveis()

    for carro in listaCarros:
        if carro["Categoria"] == CategoriaCarro and carro["Cambio"] == CambioCarro:
            #apresentacao.listar(carro)
            IdCarro = carro["Identificacao"]
            KmInicial = carro["Km"]

    DataInicio = input("Digite a data e hora atual (Formato DD/MM/AAAA XXh): ")

    locacao = apresentacao.CadastrarLocacao(IdCarro, CPF, DataInicio, KmInicial, SeguroOpcao)
    listaLocacoes.append(locacao)
    return mcsv.gravarDados('Locacao.csv', locacao.keys(), listaLocacoes)

def excluir(listaLocacoes : list, cpf : str ) -> bool:
    '''
    Excluir um cliente da lista de clientes e atualiza o arquivo CSV
    '''
    flag = False
    camposLocacao = list(listaLocacoes[0].keys())
    for i,locacao in enumerate(listaLocacoes):
        if locacao['CPF'] ==  cpf :
            flag = True
            listaLocacoes.pop(i)
    #print(listaLocacoes)
    if flag:
        mcsv.gravarDados("Locacao.csv", camposLocacao, listaLocacoes)
    return flag
    
    
            
def atualizar(listaLocacoes : list, locacao : dict) -> bool:
    '''
    Atualiza um cliente na lista de clientes e atualiza o arquivo CSV
    Parâmetros
    ----------
    listaClientes: Lista atual dos clientes
    cliente: Dicionário contendo os dados do cliente a ser atualizado
    Retorno
    -------
    Retorna True se o cliente foi atualizado com sucesso
    '''
    flag = False
    camposLocacao = list(listaLocacoes[0].keys())
    for i, existeLocacao in enumerate(listaLocacoes):
        if existeLocacao['CPF'] ==  locacao['CPF'] :
            flag = True
            listaLocacoes[i] = locacao
    if flag:
        mcsv.gravarDados("Cliente.csv", camposLocacao, listaLocacoes)
    return flag
def busca1Locacao(listaLocacoes : list, cpf : str) -> dict:
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
    for cliente in listaLocacoes:
        if cliente['CPF'] == cpf:
            return cliente
    return None
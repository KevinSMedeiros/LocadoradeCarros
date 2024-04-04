import manipulaCSV as mcsv
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
    lista = mcsv.carregarDados("LocadoradeCarros/Carro.csv")
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
    carro = apresentacao.CadastrarCarro()
    #averigua se há carro com tal placa
    if not any(c['Placa'] == carro['Placa'] for c in listaCarros):
        listaCarros.append(carro)
        print(listaCarros)
        return mcsv.gravarDados('LocadoradeCarros/Carro.csv', carro.keys(), listaCarros )  # Add the missing colon
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
    #print(listaClientes)
    if flag:
        mcsv.gravarDados("LocadoradeCarros/Carro.csv", camposCarro, listaCarros)
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
        mcsv.gravarDados("LocadoradeCarros/Carro.csv", camposCarro, listaCarros)
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
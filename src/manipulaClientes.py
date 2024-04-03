import manipulaCSV as mcsv
import apresentacao

def carregar() ->list: 
    '''
    Carrega o arquivo de Cliente.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("LocadoradeCarros/Cliente.csv")
    return lista
    

def cadastrar( listaClientes : list ) -> bool :
    '''
    Rotina para cadastrar um cliente

    Parâmetros
    ----------
    listaClientes: Lista atual dos clientes

    Retorno
    -------
    Retorna True se o cliente foi cadastrado com sucesso
    '''
    cliente = apresentacao.CadastrarCliente()
    if not any(c['CPF'] == cliente['CPF'] for c in listaClientes): 
        listaClientes.append(cliente)
        return mcsv.gravarDados('LocadoradeCarros/Cliente.csv', cliente.keys(), listaClientes )

def excluir(listaClientes : list, cpf : str ) -> bool:
    '''
    Excluir um cliente da lista de clientes e atualiza o arquivo CSV
    '''
    flag = False
    camposCliente = list(listaClientes[0].keys())
    for i,cliente in enumerate(listaClientes):
        if cliente['CPF'] ==  cpf :
            flag = True
            listaClientes.pop(i)
    #print(listaClientes)
    if flag:
        mcsv.gravarDados("LocadoradeCarros/Cliente.csv", camposCliente, listaClientes)
    return flag
    
    
            
def atualizar(listaClientes : list, cliente : dict) -> bool:
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
    camposCliente = list(listaClientes[0].keys())
    for i, existeCliente in enumerate(listaClientes):
        if existeCliente['CPF'] ==  cliente['CPF'] :
            flag = True
            listaClientes[i] = cliente
    if flag:
        mcsv.gravarDados("LocadoradeCarros/Cliente.csv", camposCliente, listaClientes)
    return flag
def busca1Cliente(listaClientes : list, cpf : str) -> dict:
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
    for cliente in listaClientes:
        if cliente['CPF'] == cpf:
            return cliente
    return None
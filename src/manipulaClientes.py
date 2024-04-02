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
    
    
            
    
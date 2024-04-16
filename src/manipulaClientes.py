import manipulaCSV as mcsv
import manipulaCarros as mcar
import manipulaLocacoes as mloc
import apresentacao

def carregar() ->list: 
    '''
    Carrega o arquivo de Cliente.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("Cliente.csv")
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
        return mcsv.gravarDados('Cliente.csv', cliente.keys(), listaClientes )

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
        mcsv.gravarDados("Cliente.csv", camposCliente, listaClientes)
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
        mcsv.gravarDados("Cliente.csv", camposCliente, listaClientes)
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

def busca1ClientePorNome(listaClientes : list, nome : str) -> dict:
    '''
    Busca um cliente na lista de clientes
    Parâmetros
    ----------
    listaClientes: Lista atual dos clientes
    nome: nome do cliente a ser buscado
    Retorno
    -------
    Retorna um dicionário com os dados do cliente
    '''
    for cliente in listaClientes:
        if cliente['Nome'] == nome:
            return cliente
    return None

def locacoesDoCliente() -> bool:
    '''
        Varre todas as locações em busca daquelas que ainda estão em andamento
        Quando encontra alguma, o algoritmo puxa todas as informações relacionadas dos outros arquivos

        No final, o valor total é calculado com base na data atual e as informações são printadas
    '''

    print("### LOCAÇÕES FINALIZADAS DO CLIENTE ###\n")

    listaCarros = mcar.carregar()
    listaLocacoes = mloc.carregar()
    listaClientes = carregar()

    escolha = int(input("Você quer pesquisar cliente por nome ou CPF?\n1.CPF\n2.Nome\n"))
    if escolha == 1:
        CPF = input("Digite o CPF do cliente: ")
    else:
        Nome = input("Digite o nome do cliente: ")

    for i in range(len(listaLocacoes)):
        locacao = mcsv.retornaNaLinha("Locacao.csv", i)  # puxa as informações da locação com o id digitado

        if escolha == 1 and CPF == locacao["CPF"]:
            valido = True
        else:
            if escolha == 2 and busca1ClientePorNome(listaClientes, Nome)['CPF'] == locacao["CPF"]:
                valido = True
            else:
                valido = False

        if valido and locacao["DataDevolucao"] != "00/00/0000 00:00":

            carro = mcar.buscaCarroPorId(listaCarros, locacao["IdCarro"])

            if escolha == 1:
                cliente = busca1Cliente(listaClientes, CPF)
            else:
                cliente = busca1ClientePorNome(listaClientes, Nome)

            if cliente is None:
                print("Erro ao carregar o cliente")

            distanciaPercorrida = int(locacao["KmFinal"]) - int(locacao["KmInicial"])

            print(f"\nID DE LOCAÇÃO: {locacao["IdLocacao"]}")
            print(f"Placa do carro: {carro["Placa"]}")
            print(f"Início da Locação: {locacao["DataInicio"]}")
            print(f"Final da Locação: {locacao["DataDevolucao"]}")
            print(f"Quilometragem percorrida: {distanciaPercorrida}")
            print(f"Valor total: {locacao["ValorTotal"]}")

    return True

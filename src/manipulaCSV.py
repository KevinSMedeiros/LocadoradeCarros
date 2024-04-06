import csv

def retornaNaLinha(nomeArquivo: str, indice: int) -> dict:
    """ Carrega do arquivo CSV um dicionário que representa os dados salvos naquela linha específica

        Parâmetros
        ----------
        nomeArquivo: nome do arquivo que contém os dados que se deseja carregar
        indice: inteiro representando a linha a ser carregada no arquivo

        Retorno
        -------
        Retorna um dicionário contendo os dados da linha desejada
        """
    # retorna um dicionario que representa as informações na linha que quiser
    with open(nomeArquivo, 'r') as arquivo:
        leitorCsv = csv.reader(arquivo, delimiter=';')

        cabecalho = next(leitorCsv)

        for i, linha in enumerate(leitorCsv):
            if i == indice:
                return {cabecalho[j]: linha[j] for j in range(len(cabecalho))}

    return {}


def pegaProximoId(nomeArquivo: str):
    """ Serve para que o id ao cadastrar um item seja 1 a mais que o anterior

        Parâmetros
        ----------
        nomeArquivo: nome do arquivo que contém os dados que se deseja carregar

        Retorno
        -------
        Retorna um inteiro representando o número de linhas detectadas
        """
    arquivo = open(nomeArquivo, 'r')
    numeroDeLinhas = len(arquivo.readlines())  # readlines gera uma lista de linhas, aí o len conta o número delas
    return numeroDeLinhas

 
def carregarDados( nomeArquivo: str) -> list : 
    ''' Carrega do arquivo CSV uma lista de informações, com cada item
    da lista sendo um dicionário

    Parâmetros
    ----------
    nomeArquivo: nome do arquivo que contém os dados que se deseja carregar 

    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados do arquivo CSV que se deseja carregar
    '''
    try:
        arq = open(nomeArquivo, "r")
        listaDados = csv.DictReader(arq, delimiter=';')
        listaDados = list(listaDados)
    except FileNotFoundError:
        print("Arquivo não encontrado ", nomeArquivo)
        return []
    return listaDados

########################################################

def  gravarDados( nomeArquivo: str, campos : list, lista : list ) -> bool :
    '''Grava a informação da lista em um arquivo CSV
    
    Parâmetros
    ----------
    nomeArquivo: nome do arquivo que contém os dados dos clientes 
    campos: campos do header arquivo CSV
    lista: lista com os dados a serem gravados

    Retorno
    -------
    Retorna True caso tenha sucesso ao gravar o cliente e 
    false caso ocorra algum erro durante a gravação
    '''
    try:
        # abrindo o arquivo a ser gravado para escrita(sobreescreve o existente)
        arq = open(nomeArquivo, "w", newline='')
        meuCSV = csv.DictWriter(arq,fieldnames=campos, delimiter=';')
        meuCSV.writeheader()        
        for r in lista:            
            meuCSV.writerow(r)
            print(r)
            arq.flush()
        arq.close()
        return True       
    except FileNotFoundError:
        print("erro na abertura do arquivo ", nomeArquivo)
        return False


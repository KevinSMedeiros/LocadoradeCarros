import csv

 
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

def gravarDados( nomeArquivo: str, campos : list, lista : list ) -> bool :
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


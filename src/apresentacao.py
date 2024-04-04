from os import system, name

#################################################################
def limpaTela():
    '''
    Limpa a tela de acordo com o sistema operacional
    '''
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

#################################################################        

def MenuPrincipal() -> int :
    '''
    Exemplo de Menu principal para o sistema
    
    Retorno    
    -------
    Retorna válida escolhida

    '''
    opcoes = [1,2,3,9]
    opcao = 10
    while opcao not in opcoes:
        limpaTela()
        print("#"*20)
        print("1.Locações\n2.Clientes\n3.Carros\n9.Sair")    
        print('#'*20)
        opcao = int(input("Opção -> "))            
    return opcao

################################################################# 
def MenuClientes() -> int :
    '''
    Exemplo de Menu para manipulação de clientes
    
    Retorno    
    -------
    Retorna válida escolhida

    '''
    opcoes = [1,2,3,4,9]
    opcao = 10
    while opcao not in opcoes:
        print("#"*20)
        print("1.Cadastrar Cliente\n2.Excluir Cliente\n3.Listar Clientes\n4.Alterar informações\n9.Sair")    
        print('#'*20)
        opcao = int(input("Opção -> "))            
    return opcao
def MenuCarros() -> int :
    '''
    Exemplo de Menu para manipulação de carros
    
    Retorno    
    -------
    Retorna válida escolhida

    '''
    opcoes = [1,2,3,4,5,9]
    opcao = 10
    while opcao not in opcoes:
        print("#"*20)
        print("1.Cadastrar Carro\n2.Excluir Carro\n3.Listar Carros\n4.Carros a venda\n5.Buscar carro por categoria\n9.Sair")    
        print('#'*20)
        opcao = int(input("Opção -> "))            
    return opcao   

def CadastrarCliente() -> dict :
    '''
    Procedimento que mostra os campos para cadastramento de um cliente
    
    Retorno
    -------
    Retorna um dicionário com as informações de um cliente    
    '''
    print("#"*30)
    print("Cadastramento de um novo cliente ")
    l = ["CPF","Nome","Nascimento","Idade","Endereco","Cidade","Estado"]
    cliente = {}
    for campo in l:
        cliente[campo] = input(f"{campo}:")
        print("#"*30)
    return cliente

#################################################################    

def CadastrarCarro() -> dict:
    '''
    Procedimento que mostra os campos para cadastramento de um carro
    
    Retorno
    -------
    Retorna um dicionário com as informações de um carro    
    '''
    print("#"*30)
    print("Cadastramento de um novo carro ")
    l = ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria", "Km", "Diaria", "Seguro", "Disponivel"]
    carro = {}
    Modelo_opcoes = ["Kwid","Polo","Renegade","T-Cross","Corola","Hillux"]
    Cor_opcoes = ["preto","cinza"]
    Cambio_opcoes = ["manual","automático"]
    Categoria_opcoes = ["Economico","Intermediario","Conforto","Pickup"]
    Disponivel_opcoes = ["True","False"]
    for campo in l:
        if campo == "Modelo":
            print(f"Modelos disponíveis: {Modelo_opcoes}")
            while carro.get(campo) not in Modelo_opcoes:
                carro[campo] = input(f"{campo}:")
        elif campo == "Cor":
            print(f"Cores disponíveis: {Cor_opcoes}")
            while carro.get(campo) not in Cor_opcoes:
                carro[campo] = input(f"{campo}:")
        elif campo == "Cambio":
            print(f"Tipos de Câmbio disponíveis: {Cambio_opcoes}")
            while carro.get(campo) not in Cambio_opcoes:
                carro[campo] = input(f"{campo}:")
        elif campo == "Categoria":
            print(f"Categorias disponíveis: {Categoria_opcoes}")
            while carro.get(campo) not in Categoria_opcoes:
                carro[campo] = input(f"{campo}:")
        elif campo == "Disponivel":
            print(f"Disponibilidade: {Disponivel_opcoes}")
            while carro.get(campo) not in Disponivel_opcoes:
                carro[campo] = input(f"{campo}:")
        else:
            carro[campo] = input(f"{campo}:")
        print("#"*30)
    return carro   
def listar(lista : list):
    '''
    Lista os elementos da lista
    '''
    for i in lista:
        print("#"*30)
        for campo in i.keys():
            print(campo, ":", i[campo])
        
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


def MenuPrincipal() -> int:
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

def MenuLocacao() -> int:
    '''
    Menu para manipulação de locações

    Retorno
    -------
    Retorna válida escolhida

    '''

    opcoes = [1, 2, 3, 9]
    opcao = 10
    while opcao not in opcoes:
        print("\n")
        print("#" * 20)
        print("1.Nova Locação\n2.Finalizar Locação\n3.Relatório de Carros Locados\n9.Sair")
        print('#' * 20)
        opcao = int(input("Opção -> "))
    return opcao

def MenuClientes() -> int:
    '''
    Exemplo de Menu para manipulação de clientes
    
    Retorno    
    -------
    Retorna válida escolhida

    '''
    opcoes = [1,2,3,4,9]
    opcao = 10
    while opcao not in opcoes:
        print("\n")
        print("#"*20)
        print("1.Cadastrar Cliente\n2.Excluir Cliente\n3.Localizar locações finalizadas\n4.Alterar informações\n9.Sair")
        print('#'*20)
        opcao = int(input("Opção -> "))
        print("\n")
    return opcao


def MenuCarros() -> int:
    '''
    Exemplo de Menu para manipulação de carros
    
    Retorno    
    -------
    Retorna válida escolhida

    '''
    opcoes = [1,2,3,4,5,9]
    opcao = 10
    while opcao not in opcoes:
        print("\n")
        print("#"*20)
        print("1.Cadastrar Carro\n2.Excluir Carro\n3.Listar Carros\n4.Carros a venda\n5.Buscar carro por categoria\n9.Sair")    
        print('#'*20)
        opcao = int(input("Opção -> "))
        print("\n")
    return opcao


#################################################################

def CadastrarCliente() -> dict:
    '''
    Procedimento que mostra os campos para cadastramento de um cliente
    
    Retorno
    -------
    Retorna um dicionário com as informações de um cliente    
    '''
    print("####### NOVO CLIENTE #######\n")
    l = ["CPF","Nome","Nascimento","Idade","Endereco","Cidade","Estado"]
    cliente = {}
    for campo in l:
        if campo != "CPF":
            cliente[campo] = input(f"{campo}:")
        else:
            cliente["CPF"] = input("Digite o CPF do cliente (apenas os números): ")
            while not VerificaCpf(cliente["CPF"]):
                cliente["CPF"] = input("CPF inválido, digite novamente: ")
    print("\n")
    return cliente


def VerificaCpf(cpf: str):
    '''
        Procedimento que verifica se o cpf recebido é válido

        Retorno
        -------
        Retorna True se o cpf é válido, False se não for válido
        '''
    dA1 = cpf[9]
    dA2 = cpf[10]

    soma = 0
    j = 10

    for i in range(9):
        soma = soma + (int(cpf[i]) * j)
        j = j - 1

    resto = soma % 11

    if resto < 2:
        dB1 = 0
    else:
        dB1 = 11 - resto

    soma = 0
    j = 11

    for i in range(10):
        soma = soma + (int(cpf[i]) * j)
        j = j - 1

    resto = soma % 11

    if resto < 2:
        dB2 = 0
    else:
        dB2 = 11 - resto

    if int(dA1) == int(dB1) and int(dA2) == int(dB2):
        return True
    else:
        return False


def CadastrarCarro(identificacao) -> dict:
    '''
    Procedimento que mostra os campos para cadastramento de um carro
    
    Retorno
    -------
    Retorna um dicionário com as informações de um carro    
    '''
    print("####### NOVO CARRO #######")

    l = ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria", "Km", "Diaria", "Seguro", "Disponivel"]
    carro = {}

    Modelo_opcoes = ["Kwid", "Polo", "Renegade", "T-Cross", "Corola", "Hillux"]
    Cor_opcoes = ["preto", "cinza"]
    Cambio_opcoes = ["manual", "automático"]
    Categoria_opcoes = ["Economico", "Intermediario", "Conforto", "Pickup"]
    #Disponivel_opcoes = ["True", "False"]

    for campo in l:

        if campo == "Identificacao":
           carro[campo] = identificacao

        elif campo == "Modelo":
            print(f"\nModelos disponíveis: {Modelo_opcoes}")
            while carro.get(campo) not in Modelo_opcoes:
                carro[campo] = input(f"{campo}:")

        elif campo == "Cor":
            print(f"\nCores disponíveis: {Cor_opcoes}")
            while carro.get(campo) not in Cor_opcoes:
                carro[campo] = input(f"{campo}:")

        elif campo == "Cambio":
            print(f"\nTipos de Câmbio disponíveis: {Cambio_opcoes}")
            while carro.get(campo) not in Cambio_opcoes:
                carro[campo] = input(f"{campo}:")

        elif campo == "Categoria":
            print(f"\nCategorias disponíveis: {Categoria_opcoes}")
            while carro.get(campo) not in Categoria_opcoes:
                carro[campo] = input(f"{campo}:")

        elif campo == "Disponivel":
            carro["Disponivel"] = "True"

        else:
            carro[campo] = input(f"\n{campo}:")

    return carro


#################################################################


def listar(lista : list):
    '''
    Lista os elementos da lista
    '''
    for i in lista:
        print("#"*30)
        for campo in i.keys():
            print(campo, ":", i[campo])

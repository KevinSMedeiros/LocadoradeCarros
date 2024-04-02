class Carro:
    def __init__(self, Identificacao: int=0, Modelo: str='', Cor: str='', AnoFabricacao: str='', Placa: str='', Cambio: str='', Categoria: str='', Km: int=0, Diaria: float=0, Seguro: float=0, Disponivel: bool=False):
        self.Identificacao = Identificacao
        self.Modelo = Modelo
        self.Cor = Cor
        self.AnoFabricacao = AnoFabricacao
        self.Placa = Placa
        self.Cambio = Cambio
        self.Categoria = Categoria
        self.Km = Km
        self.Diaria = Diaria
        self.Seguro = Seguro
        self.Disponivel = Disponivel

        
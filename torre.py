class Torre:
    def __init__(self, idtorre = 0, nome = "", endereco = ""):
        self.idtorre = idtorre
        self.nome = nome
        self.endereco = endereco

    def registrar(self, idtorre, nome, endereco):
        self.idtorre = idtorre
        self.nome = nome
        self.endereco = endereco

    def imprimir(self):
        print("Dados da Torre", "\nId da torre:" , self.idtorre , "\nNome:" , self.nome , "\nEndereço:" , self.endereco)
from torre import Torre

class Apartamento(Torre):
    def __init__(self, idtorre, nome, endereco, idap = 0, numero = "", vaga = 0):
        self.torre = Torre(idtorre, nome, endereco)
        self.idap = idap
        self.numero = numero
        self.vaga = vaga
        self.prox = None

    def registrar(self, idap, numero, vaga):
        self.idap = idap
        self.numero = numero
        self.vaga = vaga

    def imprimir(self):
        print("Dados do apartamento" , "\nId do apartamento:" , self.idap , "\nNúmero:" , self.numero , "\nVaga:" , self.vaga , "\nTorre:" , self.torre.nome)

from node import Node
from apartamento import Apartamento

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._tamanho = 0

    def verfila(self):
        if self._tamanho > 0:
            v = " "
            last = self.primeiro
            while(last):
                v = v + str(last.idap) + " "
                last = last.prox
            return v
        raise IndexError("Não há nada na fila.")

    def inserir(self, idtorre, nome, endereco, idap, numero, vaga):
        node = Apartamento(idtorre, nome, endereco, idap, numero, vaga)
        if self.ultimo is None:
            self.ultimo = node
        else:
            self.ultimo.prox = node
            self.ultimo = node

        if self.primeiro is None:
            self.primeiro = node

        self._tamanho = self._tamanho + 1

    def remover(self):
        if self._tamanho > 0:
            item = self.primeiro.idap
            self.primeiro = self.primeiro.prox
            if self.primeiro is None:
                self.ultimo = None
            self._tamanho = self._tamanho - 1
            return item
        raise IndexError("Não há nada na fila.")

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        if self._tamanho > 0:
            rep = " "
            last = self.primeiro
            while(last):
                rep = rep + str(last.idap) + " "
                last = last.prox
            return rep
        return "Não há nada na fila."

    def __str__(self):
        return self.__repr__()
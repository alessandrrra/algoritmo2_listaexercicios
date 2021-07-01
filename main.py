from torre import Torre
from apartamento import Apartamento
from fila import Fila

separador = "-----"

t = Torre()
t.registrar(1, "Torre Central", "Rua Flores, 135")
t.imprimir()

print(separador)

ap = Apartamento(1, "Torre Central", "Rua Flores, 135")
ap.registrar(1, "12", 5)
ap.imprimir()

print(separador)

ap2 = Apartamento(1, "Torre Central", "Rua Flores, 135")
ap2.registrar(2, "14", 3)
ap2.imprimir()

print(separador)

fila = Fila()
fila.inserir(1, "Torre Central", "Rua Flores, 135", 1, "10", 2)
fila.inserir(1, "Torre Central", "Rua Praia, 148", 1, "5", 5)
fila.inserir(1, "Torre Central", "Rua Flores, 135", 8, "2", 3)
fila.inserir(1, "Torre Central", "Rua Flores, 135", 6, "5", 6)
fila.inserir(1, "Torre Central", "Rua Campos, 102", 2, "1", 7)
# -*- coding: utf-8 -*-

TEMPERATURA_CRITICA = 60

class Temperatura(Exception):

    def __init__(self, temperatura):
        self._temperatura = temperatura

    def __str__(self):
        return "Se ha alcanzado la temperatura crítica: {}. Todos muertos!!!".format(self._temperatura)

def preparar_materiales(producto, temperatura):
    mezclar_elementos(temperatura)
    print ("Se ha preparado: {} a {}ºC".format(producto, temperatura))

#no se puede mezclar si se alcanza la temperatura critica
def mezclar_elementos(temperatura):
    if temperatura > 60:
        raise Temperatura(temperatura)
    pass
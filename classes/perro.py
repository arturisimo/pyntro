# -*- coding: utf-8 -*-
from mascota import Mascota

'''
    herencia: Perro hereda de mascota

'''
class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza

    def __str__(self):
       return "Nombre: {}, edad: {}".format(self._nombre, self._edad, self._raza)

    def ladrar(self):
        print ("guau guau")
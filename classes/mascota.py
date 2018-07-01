# -*- coding: utf-8 -*-

'''

	Entorno de trabajo
	python 3.6.5
	PyCharm Python IDE de jetbrains
	Jupyter Notebook es una aplicación web que permite crear y compartir documentos que contienen código fuente,
	ecuaciones, visualizaciones y texto explicativo

	Clases. Todas las clases en py heredean de object

    constructor - __init__

    this - self

    metodos dinamicos deben tener un argumento que haga referencia al propio objecto por convencion se llama self
    pero al invocar el metodo no se pasa el self

    getter de atributos:  es obligatorio poner self.
    es una convencion que los atributos de la clase comiencen por _
    en python no hay modificadores de visibilidad

    Los metodos que empiezan por __ son especiales

'''

class Mascota:

    def __init__(self, nombre, edad):
        self._nombre = nombre
        #self._edad = edad
        self.cambiar_edad(edad)

    def __str__(self):
        return "Nombre: {}, edad: {}".format(self._nombre, self._edad)

    def nombre(self):
            return self._nombre

    def edad(self):
            return self._edad

    def __str__(self):
        return "Nombre: {}, edad: {}".format(self._nombre, self._edad)


    def cambiar_edad(self,edad):
        if(edad < 0):
            print ("La edad de {} no se puede cambiar negativo".format(self._nombre))
        else:
            self._edad = edad


##################EJECUCION Mascota#########################
'''
if __name__ == '__main__':
    m = Mascota("jana", 2)
    nombre = m.nombre()
    edad = m.edad()
    m.cambiar_edad(-3)
    print(m)
'''


###########################################################

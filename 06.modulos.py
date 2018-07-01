'''
	Modulos o librerias

	Pip - administrador de paquetes de python -  pip install nombre-paquete
	PyPI o CheeseShop es el repositorio de software oficial para aplicaciones de terceros en el lenguaje de programación Python
	EasyInstall es un gestor de paquetes. Suministra un formato estándar para distribuir programas y bibliotecas en Python, 
	basado en Python eggs (anñalogo paquetes java)

'''	

#importa libreria math
import math
a = math.sin(44)

#importa funcion sin de math
from math import sin
b = sin(44)

#importa todas las funciones de math
from math import *
c = cos(44)

#importa funcion sin de math con un alias
from math import sin as s
d = s(44)

print (a,b,c,d)

from libs.recursivas import fact
a = fact(5)
print (a)

##devuelve main si se ejectuta este archivo 'standalone'
## o se ejecuta el nombre del archivo si es resultado de un import
print (__name__)

#argumentos de la ejecucion
import sys
print ("args",[ arg for arg in sys.argv])

#version de python
print ("version",sys.version,"platform",sys.platform)
# -*- coding: utf-8 -*-

''''

Escribir una clase Python llamada Fruteria con lo siguiente:
1) Un constructor que reciba el nombre de la frutería (nombre), y como segundo argumento una lista de Precios (lista Precios).
La lista de precios es un diccionario en en que la clave es la fruta y el valor el precio por kilo.
El constructor debe guardar los 2 argumento e imprimir un mensaje de bienvenida.  Por ejemplo "Bienvenido a la frutería de Ana".
2) Un método llama costePorKilo; recibe como argumento el nombre de una fruta y debe devolver el precio de esa fruta.
Si la frutería no tiene esta fruta debe imprimir un mensaje y devolver None.
3) Un método precioOrden.  Este método recibe un sólo argumento llamado orden.  El tipo de orden es una lista con tuplas de 2 elementos.  Cada una de estas tuplas tiene el mismo tipo de contenido.  Tamaño 2.   Primer elemento el nombre de una fruta, segundo elemento la cantida de kilos que se quiere de esa fruta.
El método precioOrden debe devolver el precio total de la orden.  Si no hay una fruta en el inventario no se toma en cuenta.
4) Un método frutasDisponibles.  Devuelve una lista con las frutas disponibles en el inventario.
5) Un método nombre que devuelve el nombre de la frutería.
6) Un método __str__ que devuelve un string que representa la frutería al mundo exterior.
'''

class FrutaError(Exception):

    def __init__(self, message):
        self._message = message

    def message(self):
        return self._message


class Fruteria:

    def __init__(self, nombre, precios):
        self._nombre = nombre
        self._precios = precios
        print ('Bienvenido a la fruteria de {}'.format(self._nombre))

    def __str__(self):
        return "Fruteria: {}".format(self._nombre)

    def nombre(self):
        return self._nombre

    #dict fruta - precio/kilo
    def precios(self):
        return self._precios

    # dict fruta - precio/kilo
    def coste_por_kilo(self, fruta):
        if fruta not in self._precios:
            raise FrutaError('No tenemos {}'.format(fruta))

        return self._precios.get(fruta)

    #orden tupla de 2 elementos fruta - k de fruta
    #si no hay fruta se salta
    def precio_orden(self, orden):
        precio = 0
        for fruta, kilos in orden:
            coste_por_kilo = self.coste_por_kilo(fruta)
            precio += self.coste_por_kilo(fruta) * kilos
        return precio

    def frutas_disponibles(self):
        return self._precios.keys()
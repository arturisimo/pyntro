# -*- coding: utf-8 -*-

from classes.fruteria import Fruteria, FrutaError

print( __name__ )
nombre = "La Frutería de Ana"
precios = { 'kiwis': 2.5, 'higos': 3.25, 'frambuesas': 4.75}
tienda = Fruteria(nombre, precios)

orden = [ ('kiwis', 4), ('higos', 1.5), ('platanos', 4.75)]
try:
 costeOrden = tienda.precio_orden(orden)
 print( "Precio de la orden {}€".format(costeOrden))
except FrutaError as e:
 print("Excepción: " + str(e))

print()
print("Precio de los productos en '{}'".format(tienda.nombre()))
for fruta in tienda.frutas_disponibles():
 print("\t'{}': {} euros".format(fruta, tienda.coste_por_kilo(fruta)))
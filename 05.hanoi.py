"""
	Torres de Hanoi. Ejemplo de recursividad
	mover la pila de discos de origen O a destino D ,utilizando una torre auxiliar A, de uno en uno.
	Con una condicion un disco de tamanyo inferior no puede estar debajo de uno de tamanyo mayoddr

	imprimir movimientos

"""

def hanoi(n, O, A, D) :
	if n == 1 : 
		print ('muevo',n,'de ' + O + ' a ' + D)
	else :
		hanoi(n-1, O, D, A)
		print ('muevo',n,'de ' + O + ' a ' + D)
		hanoi(n-1, A, O, D)

hanoi(3, "origen", "aux", "destino")
'''
	Funciones

'''

nombre_fichero = '../data/loudacre.log'

fichero = open(nombre_fichero, 'rt')
lineasFichero = fichero.readlines()
fichero.close()


def celsiusAFahreinheit(s): return int(s) * float(9) / 5 + 32


def convertirABool(s): return True if s == "TRUE" else False


def transformar(linea):
    lista = linea.split(",")
    lista[3] = celsiusAFahreinheit(lista[3])
    lista[4] = celsiusAFahreinheit(lista[4])
    lista[5] = int(lista[5])
    lista[6] = int(lista[6])
    lista[7] = int(lista[7])
    lista[8] = int(lista[8])
    lista[9] = convertirABool(lista[9])
    lista[12] = float(lista[12])
    lista[13] = float(lista[13])

    modelo = lista[1].split()[0]
    lista.insert(1, modelo)

    return lista


listaTemporal = [transformar(linea) for linea in lineasFichero]
tupla = tuple(listaTemporal)

print("Numero de registros: {0}".format(len(tupla)))
print("Tipo: ", type(tupla))

sorrentos = [True if registro[10] else False for registro in tupla if registro[1] == "Sorrento"]
print(len(sorrentos))
print(sorrentos.count(True))

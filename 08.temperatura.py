from classes.temperatura import Temperatura, preparar_materiales


try:
    preparar_materiales('condesador de fluzo', 57)
except Temperatura as temperatura_exception:
    print(temperatura_exception)
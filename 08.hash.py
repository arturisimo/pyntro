"""

Método __hash__ que devuelve un entero

"""
from classes.rational import Rational

f1 = Rational(3, 5)
f2 = Rational(6, 10)

if (f1 == f2):
    print(f1, f2)

f3 = Rational(6, 10)

#si quiero hacer un set con Rational
#esto devuelve TypeError: unhashable type: 'Rational'
#esto se debe a que el set en python emplea el hash para implementarse
#intenta buscar el hash del metodo pero no lo encuenta no es unhashable
print (f3)

#el set utiliza el método __repr__ si no la tiene imprime {<__main__.Rational object at 0x0000026618BD5550>}
print ({f3})


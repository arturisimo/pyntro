'''

metodo __eq__ hereda de la clase Object (todas las clases heredan de object)

Si nuestra clase no tiene el metodo __eq__ utiliza la de la clase Object que
devuelve true si los dos objetos ocupan la misma direccion de memoria


metodo __hash__
Devielve un  numero entero. Si dos objetos son iguales el hash de cada uno debe ser igual

'''


class Rational0:
    def __init__(self, n, d):
        self._n = n
        self._d = d


f1 = Rational0(3, 5)
f2 = Rational0(3, 5)

# son dos objetos que ocupan direcciones de memoria distintos
# asi pues son distintos
if (f1 != f2):
    print(f1, f2)


class Rational:
    def __init__(self, n, d):
        self._n = n
        self._d = d

    # metodo equals
    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise ValueError("No es racional")
        else:
            return self._n * other._d == self._d * other._n

    def __hash__(self):
        return self._d * self._n

    def __str__(self):
        return str(self._n) + "/" + str(self._d)

    def __repr__(self):
        return str(self._n) + "/" + str(self._d)




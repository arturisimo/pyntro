from classes.mascota import Mascota
from classes.perro import Perro

m = Mascota("jana", 2)
nombre = m.nombre()
edad = m.edad()
m.cambiar_edad(-3)
print(m)


p = Perro("can",3,"dogo")
print (p)
p.ladrar()
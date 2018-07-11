#while
anio = 2001
while anio <= 2012:
    print ("Informes del Año", str(anio))
    anio += 1

#for
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio']
for nombre in mi_lista:
    print (nombre)

#for rango de enteros
for anio in range(2001, 2013):
    print ("Informes del Año", str(anio))


#List comprenhension
device_temp=[30,33,54,34,29,49]
f_temp = [elem*9/5+32 for elem in device_temp]
print (f_temp) #> [86, 91, 129, 93, 84, 120]


#iterar varias listas con zip()
x = ['x1','x2','x3']
y = ['y1','y2']
for a,b in zip(x,y):
    print (a,b)
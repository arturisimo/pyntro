# -*- coding: utf-8 -*-
'''

 Python, es un lenguajes de programación:
    - lenguaje interpretado - no requieren de un compilador para ser ejecutados sino de un intérprete
    - de alto nivel tiene una estructura sintáctica y semántica legible y es independiente de la arquitectura del hardware
    - multiplataforma
    - de tipado dinámico - el tipo de la variable se autoasigna en tiempo de ejecución
    - multiparadigma: POO, imperativa, funcional...


Tipos básicos
    – Integers
    – Floats
    – Strings
    – Booleans

Operadores Aritméticos

	Símbolo 	Significado 		Ejemplo 		Resultado
	+ 			Suma 				a = 10 + 5 		a es 15
	- 			Resta 				a = 12 - 7 		a es 5
	- 			Negación 			a = -5 			a es -5
	* 			Multiplicación 		a = 7 * 5 		a es 35
	** 			Exponente 			a = 2 ** 3 		a es 8
	/ 			División 			a = 12.5 / 2 	a es 6.25
	// 			División entera 	a = 12.5 / 2 	a es 6.0
	% 			Módulo 				a = 27 % 4 		a es 3


Caraterísticas Python
 - Tipado dinámico
 - variables reasignables

'''

#Integer
dev_temp = 37
type(dev_temp) #<class 'int'>

dev_temp = 37.0
type(dev_temp) #<class 'float'>

#Boolean
dev_temp = True
type(dev_temp) #<class 'bool'>

dev_temp = '37'
type(dev_temp) #<class 'str'>

#asignación multiple de variables
a, b, c = 'string', 15, True
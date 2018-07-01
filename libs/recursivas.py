'''
	funciones recursivas
'''

def fact(n):
	r = 1
	for i in range(1, n+1): r *= i
	return r

assert (1 == fact(0))
assert (1 == fact(1))
assert (120 == fact(5))

def fact_recursiva(n):
	if n == 0 : return 1
	else : return n * fact_recursiva(n-1)

assert (1 == fact_recursiva(0))
assert (1 == fact_recursiva(1))
assert (120 == fact_recursiva(5))


#def suma_digitos_recursivo(n) : return int(str(n)[0]) + suma_digitos_recursivo(int(str(n)[1:]))

def suma_digitos_recursivo(n) : 
	if n<=9: return n
	else: return n%10 + suma_digitos_recursivo(n//10)	

assert (6 == suma_digitos_recursivo(1230))
assert (7 == suma_digitos_recursivo(1312))
'''
	Python generator. es una funcion iterable. Preserves the funcEonal context
	yield en Python Se usa para retornar "generators", objetos iteradores que se comportan como una lista.
	yield hace un return pero guarda el estado. vuelve al punto que se fue
'''

def f():
	yield 1
	yield 2
	for i in [-3,-4] :  yield i
	yield 90

for x in f(): print (x)

def phonegen():
	d1=d2=d3=d4=d5=d6=d7 = 0
	phonelist = []
	for d1 in range(1,10):
		for d2 in range(1,10):
			for d3 in range(1,10):
				for d4 in range(0,10):
					for d5 in range(0,10):
						for d6 in range(0,10):
							for d7 in range(0,10):
								phone = '555' + '-' + str(d1) + str(d2) + str(d3)
								phone = phone + '-' + str(d4) + str(d5) + str(d6) + str(d7)
								phonelist.append(phone)
								return phonelist


# -- test program
list_of_phones = phonegen()
for each_phone in list_of_phones:
	# send_message(each_phone)
	print (each_phone)
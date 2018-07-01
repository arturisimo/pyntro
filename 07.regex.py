'''
	Expresiones regulares
	libreria re
'''

# [ ] = delimits a group of characters, any of which are a match
# [0-9] = matches characters between zero and nine
# [^0-9] = matches any characters except zero through nine
# [0-9]* = matches number of Gmes (zero or more repeGGons)
# . = matches any character except a newline
# \s = matches any whitespace character

import re

string = "kkads dsa aadsa dasda, dasasd;adsdasas	"

# r Python raw: significa que los que vaya dentro de las comillas es literal no se interpreta
# [] es cualquier elemento individual
# \s concuerda con un espacio en blanco
# \s* 0 o + espacios en blanco
# [;,\s] representa una coma, un punto y coma o un espacio en blanco
x = re.split(r'[;,\s]\s*', string)

filesname = ['makefile','foo.c','bar.py','span.c']

files = [name for name in filesname if name.endswith('.c')]
print (files)

files = [name for name in filesname if name.endswith(('.c', '.h'))]
print (files)


text1 = '27/11/2018'
text2 = '27/11/18'

#\d un digitos
#\d+ uno o mas digitos (al menos un digito)
assert ( re.match(r'\d+/\d+/\d+', text1))
assert ( re.match(r'\d+/\d+/\d+', text2))

#\d{4} 4 digitos
#compilamos la regex y la guardamos por rendimiento
date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
date_pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
assert not ( re.match(date_pattern, '27/11/18'))
assert ( re.match(date_pattern, '27/11/2018'))

same_date_pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
m = same_date_pattern.match('27/11/2018')
#m es un Match Objects
print(m)
print (m.groups()) #tupla con todos los elementos
print (m.group(0)) #Todos los grupos
print (m.group(1)) #primer elemento

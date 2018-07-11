import re
from libs.loadfile import loadfile

'''

Print the entire record that matches

The phone we are looking for has a 4 in the first column of the second part of
the unique ID, and a b in the second column of the third part of the unique ID.
xxxxxxxx-4xxx-xbxx-xxxx-xxxxxxxxxxxx

Print the entire record that matches

'''

file = '../data/loudacre.log'

lines = loadfile(file)

id_pattern = re.compile(r'.{8}-4.{3}-.b.{2}-.{12}')

#lines_match = filter(lambda x: re.match(id_pattern, x), [ line.split(',')[2] for line in lines])
lines_match = [line for line in lines if re.match(id_pattern, line.split(',')[2])]

print (lines_match)
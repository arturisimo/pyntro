'''
	List - (list) - A serial collection of objects - list = []
	Tuple (tuple) - colección inmutable - tuple = ()
	Set - (set) colección de elementos desordenada cuyos elementos son únicos set = {4,9} (2.7+) // set = set([1,2]) (2.6) (equivalente a cojunto matematico)
	Frozenset (frozenset) set inmutable frozenset = frozenset([1,2,3,0,-1])
	Dictionary (dict) An ordered collection of unique key-value object pairs dict = {'key1':'value1', 'key2':'value2'}
	
'''

#lista
l = [1, 2, True, "python"]
type(l) #<class 'list'>

#tupla
t = (1, 2, True, "python")
type(t) #<class 'tuple'>

#set
s = (1, 2, True, "python")
type(s) #<class 'tuple'>

#lista vs set
def number_repeated(lista) : return len(lista) > len(set(lista))

#set
s = (1, 2, True, "python")
type(s) #<class 'tuple'>

#frozenset
fs = frozenset({1, 2, 3, 4, 5})
type(fs) #< type 'frozenset' >

#dict
d = {'key1':'value1', 'key2':'value2'}
type(fs) #<class 'dict'>
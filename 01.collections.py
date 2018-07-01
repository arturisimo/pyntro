'''
	List - (list) A serial collection of objects - list = []
	Tuple (tuple) - An immutable collection of objects  - tuple = ()
	Set - (set) An unordered collection of unique objects set = {4,9} (2.7+) // set = set([1,2]) (2.6) (equivalente a cojunto matematico)
	Frozenset (frozenset) An immutable ordered collection of unique objects frozenset = frozenset([1,2,3,0,-1])
	Dictionary (dict) An ordered collection of unique key-value object pairs dict = {'key1':'value1', 'key2':'value2'}
	
'''

def number_repeated(lista) : return len(lista) > len(set(lista))
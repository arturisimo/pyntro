# -*- coding: utf-8 -*-
from functools import reduce  # en python3 reduce se encuentra en modulo functools

'''

Cuando tenemos que realizar operaciones sobre colecciones se puede utilizar funciones Map, Reduce, y Filter.

función lambda (funciones anónimas) se utilizan principalmente en combinación con las funciones Map, Filter y Reduce. - lambda argument_list : expression

filter - filtrar todos los elementos de una lista, para los que la función de función devuelve True
map - toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función aplicada a cada argumento
reduce -  reduce los valores de la lista a un solo valor aplicando una funcion reductora

'''


# filter#######
def filter_long6(list): return filter(lambda x: len(x) < 6, list)


# map#######
def map_percent(list): return map(lambda c: float(c) / 100.0, list)


# reduce#######
def reduce_dict_sumvalues(dict): return reduce(lambda x, y: x + y, dict.values())


def max_reduce(list): return reduce(lambda x, y: x if x > y else y, list)


def max_no_reduce(list): return max(list)


def join_inverted_reduce(list, separator): return reduce(lambda x, y: y + separator + x, list)


def join_inverted(list, separator): return separator.join(reversed(list))


# suma de numeros positivos y negativos
def sum_separator_reduce(list): return reduce(lambda x, z: (x[0], x[1] + z) if z > 0 else (x[0] + z, x[1]), list,
                                              (0, 0))


# def sum_separator_reduce_dos(list) : return reduce(lambda (x,y),z: (x, y+z) if z > 0 else (x+z, y) , list, (0,0))

# devuelve la suma de los positivos y el numero de positivos de una lista de enteros
def sum_positivos_reduce(list): return reduce(lambda x, z: (x[0] + z, x[1] + 1) if z > 0 else x, list, (0, 0))


enteros = ['32', '46', '18', '76', '23', '49', '91', '87']
palabras = ['iFruit', 'Sorrento', 'Titanic', 'Ronin', 'MeToo']
diccionario = {'MeToo': 7, 'Ronin': 7, 'Sorrento': 15, 'Titanic': 11, 'iFruit': 7}

print(reduce_dict_sumvalues(diccionario))
print(join_inverted(palabras, '::'))

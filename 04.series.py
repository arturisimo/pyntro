'''

	Ejercicio Generator: Stern series

'''


def sum_digits(x): return sum([int(char) for char in str(x)])


def stern(minnum, maxnum):
    return [(x, float(x) / sum_digits(x)) for x in range(minnum, maxnum)]


sterns = stern(1, 500)
print(sterns[480])


def stern_generator(minnum, maxnum):
    for x in range(minnum, maxnum):
        yield (x, x / sum_digits(x))


sterns_generator = [x for x in stern_generator(1, 500)]
dict_sterns_generator = dict(sterns_generator)
print(481,dict_sterns_generator[481])

def stern_generator_2(minnum, maxnum):
    yield [(x, x / sum_digits(x)) for x in range(minnum, maxnum)]

sterns_generator_2 = [x for x in stern_generator_2(1, 500)]

print(sterns_generator_2[0][480])

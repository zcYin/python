from functools import reduce

def fn(x,y):
	return x * y
def prod(L):
	return reduce(fn,L)

print('3 *5 * 7 * 9 =',prod([3,5,7,9]))
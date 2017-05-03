def do_main():
	for n in prime():
		if n < 1000:
			print(n)
		else:
			break

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisble(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisble(n),it)

if __name__ == '__main__':
	main()
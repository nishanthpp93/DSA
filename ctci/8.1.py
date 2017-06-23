# recursion
def fib(n):
	if n == 1 or n == 0:
		return 1
	else:
		return fib(n-1) + fib(n-2)

# memoization
def _fib(n, fibMemo):
	if fibMemo[n]:
		return fibMemo[n]
	else:
		fibMemo[n] = _fib(n-1, fibMemo) + _fib(n-2, fibMemo)
		return fibMemo[n]

def fib(n):
	if n == 0 or n == 1:
		return 1
	fibMemo = [0] * (n+1)
	fibMemo[0] = 1
	fibMemo[1] = 1
	return _fib(n, fibMemo)

# iteration
def fib(n):
	if n == 0 or n == 1:
		return 1
	a, b = (1,) * 2
	for i in xrange(1, n):
		c = a + b
		a = b
		b = c
	return b

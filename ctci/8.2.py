import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

# rearranging rights and downs
def countPaths(m):
	return ncr(len(m)+len(m[0])-2, len(m[0])-1)

# memoization for blockades
def countPaths(m):
	p = [[1 for cols in m[0]] for rows in m]
	for i in xrange(1,len(p)):
		for j in xrange(1,len(p[0])):
			p[i][j] = p[i][j-1] + p[i-1][j]
	return p[len(p)-1][len(p[0])-1]


def makeZeros(m):
	rows, cols = [], []
	print rows, cols
	for i in xrange(len(m)):
		for j in xrange(len(m[i])):
			if m[i][j] == 0:
				rows.append(i)
				cols.append(j)
	rows = list(set(rows))
	cols = list(set(cols))
	for i in xrange(len(m)):
		for j in xrange(len(m[i])):
			if i in rows or j in cols:
				m[i][j] = 0
	return m
def rotate(m):
	for j in xrange(len(m[0])/2):
		if len(m[j])%2 == 1:
			x = len(m[j])/2+1
		else:
			x = len(m[j])/2
		for i in xrange(x):
			temp = m[j][i]
			m[j][i] = m[i][len(m[0])-j-1]
			m[i][len(m[0])-j-1] = m[len(m[0])-j-1][len(m[j])-i-1]
			m[len(m[0])-j-1][len(m[j])-i-1] = m[len(m[j])-i-1][j]
			m[len(m[j])-i-1][j] = temp
	return m
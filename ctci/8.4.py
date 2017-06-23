def _permute(s, l, r):
	if l == r:
		print ''.join(s)
	else:
		for i in xrange(l, r+1):
			s[l], s[i] = s[i], s[l]
			_permute(s, l+1, r)
			s[l], s[i] = s[i], s[l]
 
def permute(s):
	_permute(list(s), 0, len(s)-1)

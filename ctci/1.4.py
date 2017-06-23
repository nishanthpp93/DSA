def charCounts(s):
	d = {}
	u = ''
	for char in s:
		if d.get(char):
			d[char]+=1
		else:
			d[char] = 1
	return d

def cmpDicts(s1, s2):
	if charCounts(s1) == charCounts(s2):
		return True
	else:
		return False
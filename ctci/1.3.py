def getUniqueChars(s):
	d = {}
	u = ''
	for char in s:
		if d.get(char):
			pass
		else:
			d[char] = 1
			u+=char
	return u
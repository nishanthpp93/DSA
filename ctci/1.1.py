def hasUniqueChars(s):
	d = {}
	for char in s:
		if d.get(char):
			return False
		else:
			d[char] = 1
	return True

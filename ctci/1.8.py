def checkRotated(s1, s2):
	if len(s1) != len(s2):
		return False
	elif s1 not in s2+s2:
		return False
	else:
		return True
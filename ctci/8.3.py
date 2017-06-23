def powersetGen(nums):
	n = len(nums)
	powerset = []
	for i in xrange(1<<n):
		subset = []
		for j in xrange(n):
			if (i>>j) & 1 == 1:
				subset.append(nums[j])
		powerset.append(subset)
	return powerset
def _fill(m, i, j, old, new):
	if i < 0 or i > len(m[j]) - 1 or j < 0 or j > len(m) - 1:
		return
	if m[i][j] == old:
		m[i][j] = new
		_fill(m, i-1, j, old, new)
		_fill(m, i+1, j, old, new)
		_fill(m, i, j-1, old, new)
		_fill(m, i, j+1, old, new)

def fill(m, old, new):
	_fill(m, 0, 0, old, new)
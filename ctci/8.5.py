def _paren(output, open, close, n):
    if open == n and close == n:
        print output
    else:
        if open<n:
            _paren(output+'(', open+1, close, n)
        if close<open:
            _paren(output+')', open, close+1, n)
            
def paren(n):
	_paren('',0,0,n)

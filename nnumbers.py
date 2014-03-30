def nNumbers(n):
    if n == 1:
        print '1',
    else:
        nNumbers(n-1)
        print str(n),
        

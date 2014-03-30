def printStack(depth):
    if depth == 1:
        print '1'
    else:
        print str(depth)
        printStack(depth - 1)

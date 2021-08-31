def findv(A, v):
    '''
    Params: Sequence A, value v
    Returns: Index of value v or NIL 
    '''
    while len(A) >= 0 and v in A:
        print(f'value {v} ')
        
A = list(range(1001))
findv(A, 55)

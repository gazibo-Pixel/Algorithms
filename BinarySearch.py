def binarySearch(n, L, right = None, left = 0, ):
    right = len(L) -1
    while  left < right <= len(L):
        mid = (left + right) // 2
        if L[mid] == n:
            print (f'Item {n} found on location {L.index(n)}')   
        if L[mid] > n:
            return binarySearch (n, L, right = mid -1)
        elif L[mid] < n:
            return binarySearch (n, L, left = mid + 1)
    return print('Item Not Found')


L = [1,2,4,8,16,32,64,128,1000]
binarySearch(16, L)
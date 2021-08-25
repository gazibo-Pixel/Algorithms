def sorting(A):
    for j in range(1, len(A)):
        key = A[j]
        print('--'*18)
        print('iteration j={} and The value form the array is A[j] = {} and the key is {}'.format(j, A[j], key))
        i = j-1
        while i >= 0 and key < A[i] :
            A[i+1] = A[i]
            print('****** ALERT SWAP HAPPEN ******')
            print(f'For i equals {i}')
            print(f'A[i+1] is {A[i+1]}')
            print(f'A[i] is {A[i]}')
            print('*'*18)
            i-=1
        A[i+1] = key
        print('~'*18)
        print(f'The value of i at this point is {i}')
        print('Mysrious line here, iteration j= {}, A[{}+1] = {} and key = {}'.format(j, i, A[i+1], key))
        print('-_'*18)
arr = [12, 11, 13, 5, 6]
sorting(arr)
# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("%d" %arr[i])
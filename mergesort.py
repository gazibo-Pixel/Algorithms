def swap(lst, left, right):
    lst[left], lst[right] = lst[right], lst[left]

def merge(lst, left, mid, right):
    i = left
    j = right
    temp = []
    while i <= mid and j <= right:
        if lst[i] < lst[j]:
            temp.append(lst[i])
            i+=1
        elif lst[j] < lst[i]:
            temp.append(lst[j])
            j+=1
        if i < mid:
            pass
        if j < right:
            pass

def mergesort(lst, left, right):
    if left >= right :
        return
    elif left +1 == right:
        if lst[left] > lst[right]:
            print(f'swap hapnning  thr list is {lst}')
            swap(lst, left, right)
        return
    else:
        mid = (left + right) //2
        mergesort(lst, left, mid)
        mergesort(lst, mid+1, right)
        merge(lst, left, mid, right)

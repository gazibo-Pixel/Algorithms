def binarySearchHelper(lst, elt, left, right):
    n = len(lst)
    if (left > right):
        return None
    else:
        mid = (left + right) //2
        if elt == mid:
            return mid
        elif lst[mid] < elt:
            return binarySearchHelper(lst, elt, mid+1, right)
        else:
            return binarySearchHelper(lst, elt, left, mid-1)
def binarysearch(lst, elt):
    n = len(lst)
    if elt < lst[0] or elt > lst[n-1]:
        return None
    else:
        binarySearchHelper(lst, elt, 0, n-1)

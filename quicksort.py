__author__ = 'ardila'

s = [int(i) for i in open('QuickSort.txt', mode='r').read().split('\r\n')[:-1]]


import math
def middle(a,b,c):
    if a>b:
        if b>c:
            return 1
        elif a>c:
            return 2
        else:
            return 0
    elif a>c:
        return 0
    elif b>c:
        return 2
    else:
        return 1


def choose_pivot(A, l, r, pivot_type):
    if pivot_type == 'first':
        return l
    elif pivot_type == 'last':
        return r
    elif pivot_type == 'median_of_three':
        m = (r-l)/2
        return [l,m,r][middle(A[l], A[m], A[r])]
    else:
        print 'Pivot type %s not recognized'%pivot_type
        raise ValueError



def partition(A, l, r, pivot_type):
    i = l+1
    j = l+1
    pivot_ind = choose_pivot(A, l,r, pivot_type)
    pivot = A[pivot_ind]
    A[l], A[pivot_ind] = A[pivot_ind], A[l]
    while j < len(A):
        if A[j]<pivot:
            A[i], A[j] = A[j], A[i]
            i +=1
        j += 1
    A[l], A[i-1] = A[i-1], A[l]
    return i-1

def quicksort_call(A, l, r, comparisons, pivot_type):
    if l<r:
        comparisons += r-l
        p = partition(A, l, r, pivot_type)
        comparisons = quicksort_call(A, l, p-1, comparisons, pivot_type)
        comparisons = quicksort_call(A, p+1, r, comparisons, pivot_type)
    return comparisons



def quicksort(A, pivot_type='first'):
    l = 0
    r = len(A)-1
    return quicksort_call(A, l, r, 0, pivot_type)
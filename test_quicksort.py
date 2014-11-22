__author__ = 'ardila'

from quicksort import quicksort, middle
import numpy as np
import itertools
test_case = list(np.random.randint(1, 1000, 10))
sorted_test_case = sorted(test_case)
quicksort(test_case)
for t, s in zip(test_case, sorted_test_case):
    assert t == s

comparisons = quicksort(range(10))
assert comparisons == 5*9

test_case_2 = range(10)+[5]
#test_case_2.reverse()
print test_case_2
print quicksort(test_case_2, 'last')
test_case_2 = range(10)+[5]
print quicksort(test_case_2)

for order in itertools.permutations([0,1,2]):
    m = order.index(1)
    test_m = middle(*order)
    assert m == test_m


a = [int(i) for i in open('QuickSort.txt', mode='r').read().split('\r\n')[:-1]]
print quicksort(a)
a = [int(i) for i in open('QuickSort.txt', mode='r').read().split('\r\n')[:-1]]
print quicksort(a, 'last')
a = [int(i) for i in open('QuickSort.txt', mode='r').read().split('\r\n')[:-1]]
print quicksort(a, 'median_of_three')

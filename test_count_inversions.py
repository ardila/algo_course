__author__ = 'ardila'
from count_inversions import *

tests =[([1,2,3,4,5,6], 0),
        ([1,3,2], 1),
        ([1,3,4,5,2], 3),
        (range(100)+[-1], 100)]

for test_val, answer in tests:
    sorted, count = merge_and_count_inversions(test_val)
    assert count==answer


print merge_and_count_inversions(a)[1]

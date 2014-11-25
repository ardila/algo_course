__author__ = 'ardila'

import heapq

answer=0
f = open('Median.txt','r')
inf = float('inf')
heap_small = [inf]
heap_large = [inf]
for i in f.readlines():
    i = int(i)
    m1 = heap_small[0]*-1
    m2 = heap_large[0]
    if i>m1:
        heapq.heappush(heap_large, i)
    else:
        heapq.heappush(heap_small, -i)
    if len(heap_small)>len(heap_large)+1:
        i = heapq.heappop(heap_small)*-1
        heapq.heappush(heap_large,i)
    if len(heap_large)>len(heap_small):
        i = heapq.heappop(heap_large)*-1
        heapq.heappush(heap_small,i)
    m = heap_small[0]*-1
    answer+=m
print answer%10000

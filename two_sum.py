__author__ = 'ardila'
from collections import Counter
f = [int(line) for line in open('algo1%2Fprogramming_prob%2F2sum.txt', 'r').read().split()]
# cnt = Counter(f)
# nums = cnt.keys()
# print len(nums)
# ts_hit = 0
# not_found = {k:True for k in range(-10000, 10000+1)}
# for i, x in enumerate(nums):
#     if i%100 == 0:
#         print float(i/len(nums))
#         print len(not_found)
#     targets = not_found.keys()
#     for t in targets:
#         if (t/2. == x):
#             if (cnt[x] >= 2):
#                 del not_found[t]
#         elif cnt.get(t-x, 0)>0:
#             del not_found[t]

X = sorted(f)
i = 0
j = len(X)-1
max_t = 10000
min_t = -10000
ts = range(min_t, max_t+1)
hit = []

while i<j:
    t = X[i]+X[j]
    while t>max_t:
        j -= 1
        t = X[i]+X[j]
    old_j = j
    while t>=min_t:
        hit.append(t)
        j -= 1
        t = X[i]+X[j]
    i += 1
    j = old_j

print len(list(set(hit)))

__author__ = 'ardila'
import numpy as np
import copy
from randomized_contraction import *

edges_right = [[e] for e in range(1,10)]
edges_right.append([])
nodes = range(10)
G = {n:e for n,e in zip(nodes, edges_right)}
edges_left = [[]]
edges_left.extend([[e] for e in range(0,9)])
[G[n].extend(e) for n,e in zip(nodes, edges_left)]
assert random_contract(G, np.random.RandomState(0)) == 1

lines = [line.split() for line in open('kargerMinCut.txt', 'r').readlines()]
G_master = {int(l[0]): [int(e) for e in l[1:]] for l in lines}
min_cut_val = 1000
# 1000 is overkill, but shows solutions as you go :)
for i in range(1000):
    G = copy.deepcopy(G_master)
    cut_val = random_contract(G, np.random.RandomState(i))
    if cut_val<min_cut_val:
        print cut_val
        min_cut_val = cut_val
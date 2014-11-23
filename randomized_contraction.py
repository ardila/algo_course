__author__ = 'ardila'
import numpy as np

def merge_nodes(i,j, G, equiv):
    small, large = tuple(sorted([i,j]))
    # Merge nodes
    G[small].extend(G.pop(large))
    #Update equivalency classes
    equiv[large]['map'] = small
    equiv[small]['set'].extend(equiv[large]['set'])
    for e in equiv[large]['set']:
        equiv[e]['map'] = small
    # Remove self loops
    G[small] = [e for e in G[small] if equiv[e]['map'] != small]


def count_edges(G,equiv):
    assert len(G[G.keys()[0]]) == len(G[G.keys()[1]])
    return len(G[G.keys()[0]])


def random_contract(G, rng, equiv=None):
    if equiv is None:
        equiv = {n: {'map': n, 'set':[n]} for n in G.keys()}
    if len(G.keys()) == 2:
        return count_edges(G, equiv)
    else:
        i = rng.choice(G.keys(), 1)[0]
        j = equiv[rng.choice(G[i])]['map']
        merge_nodes(i, j, G, equiv)
        return random_contract(G, rng, equiv)

_author__ = 'ardila'

import cPickle
import numpy as np
load_from_text = False
from collections import defaultdict

def DFS_loop(G, order, N_vertices):
    leaders = np.zeros(N_vertices)
    visited = np.zeros(N_vertices)
    finish_times = np.zeros(N_vertices)
    t = 0
    for v in order:
        if not visited[v]:
            visited, t, finish_times, l, leaders = DFS(G, v, visited, t, finish_times, leaders)
    return finish_times, leaders


def DFS(G, v, visited, t, finish_times, leaders):
        l = int(v)
        to_explore = [v]
        visited[v] = 1
        explored = []
        while len(to_explore)>0:
            v = to_explore.pop()
            explored.append(v)
            leaders[l] += 1
            for w in G.get(v, []):
                if not visited[w]:
                    visited[w] = 1
                    to_explore.append(w)

        while len(explored)>0:
            w = explored.pop()
            t += 1
            finish_times[w] = t
        return visited, t, finish_times, l, leaders

def kosaraju(f):
    load_from_text = True
    if load_from_text:
        f = open('SCC.txt', 'r').readlines()

        G = defaultdict(list)
        G_r = defaultdict(list)
        for line in f:
            e1, e2 = tuple([int(e)-1 for e in line.split()])
            G[e1].append(e2)
            G_r[e2].append(e1)
        print 'Saving to disk'
        cPickle.dump(G, open('forward_SCC', 'wb'))
        cPickle.dump(G_r, open('reverse_SCC', 'wb'))
    else:
        print 'Loading from disk'
        G = cPickle.load(open('forward_SCC', 'rb'))
        G_r = cPickle.load(open('reverse_SCC', 'rb'))
        print 'Loaded'


    N_vertices = max([max(G.keys()), max(G_r.keys())])+1
    order1 = range(N_vertices)
    order1.reverse()
    print 'Loop 1'
    finish_times1, _ = DFS_loop(G_r, order1, N_vertices)
    print finish_times1
    order2 = list(np.argsort(-1*np.array(finish_times1)))
    print 'Loop 2'
    finish_times2, leaders = DFS_loop(G, order2, N_vertices)

    cluster_sizes = leaders

    print int(sum(cluster_sizes))
    print N_vertices
    answer = list(np.sort(cluster_sizes))
    answer.reverse()
    print [int(a) for a in answer[:10]]







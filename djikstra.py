__author__ = 'ardila'
from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    nodes = set(graph.nodes)
    visited = {initial:0}
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                if visited[node]<min_node:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances(min_node, edge)
            if edge not in visited or weight<visited[edge]:
                visited[edge] = weight
    return visited

f = open('dijkstraData.txt', 'r').readlines()
G = Graph()
for line in f:
    l = line.split()
    from_node = int(l[0])
    G.add_node(from_node)
    for edge in l[1:]:
        edge = edge.split(',')
        to_node = int(edge[0])
        distance = int(edge[1])
        G.add_edge(from_node, to_node, distance)

visited, path = dijkstra(G, 1)
answer_inds = [7,37,59,82,99,115,133,165,188,197]
answer = ','.join([str(visited[i]) for i in answer_inds])
print answer






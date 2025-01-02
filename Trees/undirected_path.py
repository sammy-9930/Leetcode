def undirected_path(edges, src, dst):
    graph = build_adjacency_list(edges)
    return has_path(graph, src, dst, set())

def build_adjacency_list(edges):
    graph = {}
    for edge in edges:
        a, b = edge 
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False 
    visited.add(src)
    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst, visited):
            return True 
    return False 


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

graph = build_adjacency_list(edges)
print(undirected_path(edges, 'j', 'm')) #True 
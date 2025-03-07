"""
Handling cycles in undirected graphs.
Time complexity: O(e) e-> no of edges
Space complexity: O(n) n-> no of nodes
"""

def has_path(graph, nodeA, nodeB):
    stack = [nodeA]
    visited = set()
    while stack:
        current = stack.pop()
        visited.add(current)
        if current == nodeB:
            return True 
        for neighbour in graph[current]:
            if neighbour not in visited:
              stack.append(neighbour)
    return False 
    
  
def has_path_recursive(graph, nodeA, nodeB, visited):
    if nodeA in visited:
        return False 
    visited.add(nodeA)
    for neighbour in graph[nodeA]:
        if has_path_recursive(graph, neighbour, nodeB, visited):
            return True 
    return False


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


def bidirectional_graph(edges):
    graph = build_adjacency_list(edges)
    print(has_path(graph, 'j', 'm')) #True 
    print(has_path(graph, 'm', 'j')) #True
    print(has_path(graph, 'l', 'j')) #True


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

bidirectional_graph(edges)



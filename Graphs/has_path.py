from collections import deque

"""
Return True if there is a path from source to destination.
Return False otherwise.
"""
def has_path_dfs_iterative(graph, src, dest):
    # DFS implementation
    stack = [src]
    while stack:
        current = stack.pop()
        if current == dest:
            return True 
        for neighbour in graph[current]:
            stack.append(neighbour)
    return False

def has_path_bfs_iterative(graph, src, dest):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dest:
            return True 
        for neighbour in graph[current]:
            queue.append(neighbour)
    return False 

def has_path_dfs_recursive(graph, src, dst):
  if src == dst:
    return True 
  for neighbour in graph[src]:
    if has_path_dfs_recursive(graph, neighbour, dst) == True:
      return True 
  return False

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
print("Has path:")
print(has_path_dfs_iterative(graph, 'f', 'k')) #True
print(has_path_dfs_iterative(graph, 'f', 'j')) #False 
print(has_path_bfs_iterative(graph, 'i', 'h')) #True 
print(has_path_bfs_iterative(graph, 'f', 'j')) #False
from collections import deque

def has_path(graph, src, dst):
    stack = [src]
    while stack:
        current = stack.pop()
        if current == dst:
            return True 
        for neighbour in graph[current]:
            stack.append(neighbour)
    return False 

def has_path_bfs(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True 
        for neighbour in graph[current]:
            queue.append(neighbour)
    return False 
    
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
print(has_path(graph, 'f', 'k')) #True
print(has_path(graph, 'f', 'j')) #False 
print(has_path_bfs(graph, 'i', 'h')) #True
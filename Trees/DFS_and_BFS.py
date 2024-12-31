from collections import deque

def dfs_iterative(graph, node):
    stack = [node]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current, end=' ')
            visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)

def dfs_recursive(graph, node):
    print(node, end = ' ')
    for neighbour in graph[node]:
        dfs_recursive(graph, neighbour)

def bfs_iterative(graph, node):
    visited = set()
    queue = deque([node])
    visited.add(node)
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

     
graph = {
    'A': ['B', 'C'],
    'B': ['D'], 
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

print("DFS traversal iterative: ")
dfs_iterative(graph, 'A')
print("\nDFS traversal recursive: ")
dfs_recursive(graph, 'A')
print("\nBFS: ")
bfs_iterative(graph, 'A')

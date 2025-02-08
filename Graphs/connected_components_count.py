from collections import deque
"""
Time complexity: O(e)
Space complexity: O(n)

Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
The function should return the number of connected components within the graph.
"""
def connected_components_count(graph):
    count = 0
    visited = set()
    for node in graph:
        if node not in visited:
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)
            count += 1 
    return count 

def connected_components_count_bfs(graph):
    count = 0 
    visited = set()
    for key in graph:
        if key not in visited:
            queue = deque([key])
            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                for neighbour in graph[current]:
                    if neighbour not in visited:
                        queue.append(neighbour)
            count += 1 
    return count 

graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

graph_1 = {
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}

print(connected_components_count(graph)) #2
print(connected_components_count_bfs(graph_1)) #1
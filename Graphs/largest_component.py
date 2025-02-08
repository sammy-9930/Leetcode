"""
Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph.

No of nodes in a component

"""

def largest_component(graph):
  largest = 0 
  visited = set()
  for node in graph:
    if node not in visited:
      stack = [node]
      cur_count = 0
      while stack:
        current = stack.pop()
        if current not in visited:
          visited.add(current)
          cur_count += 1 
        for neighbour in graph[current]:
          if neighbour not in visited:
            stack.append(neighbour)
        largest = max(largest, cur_count)
  return largest


def explore_size(graph, node, visited):
  if node in visited:
    return 0 
  visited.add(node)
  size = 1 #initializing cur_size to one including new node 
  for neighbour in graph[node]:
    size += explore_size(graph, neighbour, visited)
  return size 

def largest_component_recursive(graph):
  longest = 0
  visited = set()
  for node in graph:
    cur_size = explore_size(graph, node, visited)
    longest = max(cur_size, longest)
  return longest

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

print(largest_component(graph)) #4 
print(largest_component_recursive(graph_1)) #6
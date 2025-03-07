from collections import deque

def depth_first_traversal_iterative(graph, node):
    # initialize stack with startting node 
    stack = [node]
    while stack:
        current = stack.pop()
        print(current, end=' ')
        for neighbour in graph[current]:
            stack.append(neighbour)

def depth_first_traversal_recursive(graph, node):
    print(node, end=' ')
    for neighbour in graph[node]:
        depth_first_traversal_recursive(graph, neighbour)

def breadth_first_iterative(graph, node):
    """
    queue.pop(), which removes elements from the end of the queue.
    This results in a Depth-First Search (DFS) behavior instead of Breadth-First Search (BFS).
    BFS requires removing elements from the front of the queue, so you should use queue.popleft() instead.
    """
    queue = deque([node])
    while queue:
        # removing elements from front of queue 
        current = queue.popleft()
        print(current, end=' ')
        for neighbour in graph[current]:
            queue.append(neighbour)

graph = {
    'a': ['c', 'b'], 
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print("DFS traversal iterative: ")
depth_first_traversal_iterative(graph, 'a')
print("\nDFS traversal recursive: ")
depth_first_traversal_recursive(graph, 'a')
print("\nBFS traversal iterative: ")
breadth_first_iterative(graph, 'a')
# BFS recursive not possible 
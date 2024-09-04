from collections import deque

graph = {
    'a': ['b', 'c'],
    'b': ['e', 'g'],
    'c': ['f'],
    'd': ['a', 'b', 'c', 'e'],
    'e': ['f', 'd'],
    'f': [],
    'g': ['e', 'f']
}


def dfs(start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph[node]:
                stack.append(neighbor)
    
    print()


def bfs(start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph[node]:
                queue.append(neighbor)
    
    print()


print("Depth-First Search (DFS):")
dfs('a')

print("\nBreadth-First Search (BFS):")
bfs('a')

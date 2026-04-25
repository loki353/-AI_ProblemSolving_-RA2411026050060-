import time
from collections import deque

def bfs(graph, start, goal):
    """
    Finds the shortest path from start to goal using Breadth-First Search.
    """
    start_time = time.perf_counter()
    queue = deque([[start]])
    visited = set([start])
    explored_nodes = []

    if start == goal:
        return [start], [start], time.perf_counter() - start_time

    while queue:
        path = queue.popleft()
        node = path[-1]
        explored_nodes.append(node)

        if node == goal:
            end_time = time.perf_counter()
            return path, explored_nodes, end_time - start_time

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    end_time = time.perf_counter()
    return None, explored_nodes, end_time - start_time

def dfs(graph, start, goal):
    """
    Finds a path from start to goal using Depth-First Search (Iterative).
    Note: DFS does not guarantee the shortest path.
    """
    start_time = time.perf_counter()
    stack = [[start]]
    visited = set()
    explored_nodes = []

    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node in visited:
            continue
            
        explored_nodes.append(node)
        visited.add(node)

        if node == goal:
            end_time = time.perf_counter()
            return path, explored_nodes, end_time - start_time

        # Reverse neighbors to maintain a consistent order (optional)
        neighbors = list(graph.get(node, []))
        neighbors.reverse() 
        
        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    end_time = time.perf_counter()
    return None, explored_nodes, end_time - start_time

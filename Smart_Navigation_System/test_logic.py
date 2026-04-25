from algorithms import bfs, dfs
from graph_manager import GraphManager

def test_system():
    gm = GraphManager()
    # Sample graph: A connected to B, C. B to E. C to E. E to F.
    # Shortest path A-E is A-B-E or A-C-E (Length 3)
    graph_input = "A-B, A-C, B-E, C-E, E-F"
    gm.parse_input(graph_input)
    adj = gm.get_adjacency_list()
    
    start, goal = "A", "F"
    
    print(f"Testing graph: {graph_input}")
    print(f"Start: {start}, Goal: {goal}")
    
    # BFS
    path_bfs, explored_bfs, time_bfs = bfs(adj, start, goal)
    print(f"\nBFS Path: {path_bfs}")
    print(f"BFS Explored Nodes: {len(explored_bfs)}")
    
    # DFS
    path_dfs, explored_dfs, time_dfs = dfs(adj, start, goal)
    print(f"\nDFS Path: {path_dfs}")
    print(f"DFS Explored Nodes: {len(explored_dfs)}")
    
    if path_bfs and len(path_bfs) <= (len(path_dfs) if path_dfs else 999):
        print("\nAssertion Passed: BFS found a path at least as short as DFS.")
    else:
        print("\nAssertion Failed: BFS path is longer than DFS path (should not happen).")

if __name__ == "__main__":
    test_system()

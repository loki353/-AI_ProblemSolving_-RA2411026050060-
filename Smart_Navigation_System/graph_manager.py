class GraphManager:
    def __init__(self):
        self.graph = {}
        self.nodes = set()

    def add_edge(self, u, v, directed=False):
        """Adds an edge between nodes u and v."""
        u, v = str(u).strip(), str(v).strip()
        if not u or not v:
            return

        self.nodes.add(u)
        self.nodes.add(v)

        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        if v not in self.graph[u]:
            self.graph[u].append(v)
        
        if not directed:
            if u not in self.graph[v]:
                self.graph[v].append(u)

    def get_adjacency_list(self):
        return self.graph

    def get_nodes(self):
        return sorted(list(self.nodes))

    def clear(self):
        self.graph = {}
        self.nodes = set()

    def parse_input(self, input_text, directed=False):
        """Parses input in format 'A-B, B-C' or 'A->B, B->C'."""
        self.clear()
        # Handle multiple separators
        pairs = input_text.replace(',', ' ').split()
        for pair in pairs:
            if '->' in pair:
                u, v = pair.split('->')
                self.add_edge(u, v, directed=True)
            elif '-' in pair:
                u, v = pair.split('-')
                self.add_edge(u, v, directed=directed)
            else:
                # If only a node name is provided
                self.nodes.add(pair.strip())
                if pair.strip() not in self.graph:
                    self.graph[pair.strip()] = []

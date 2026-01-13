import random
import copy
import math

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # dict: vertex -> list of adjacent vertices
        self.edges = []  # list of (u,v) edges
        self._build_edges()
    
    def _build_edges(self):
        """Build edge list from adjacency lists"""
        self.edges = []
        visited = set()
        for u in self.vertices:
            for v in self.vertices[u]:
                if (v, u) not in visited:
                    self.edges.append((u, v))
                    visited.add((u, v))
    
    def contract(self, u, v):
        """
        Contract vertices u and v into u
        Remove v and merge its adjacency list into u
        """
        # Merge v's neighbors into u
        self.vertices[u].extend(self.vertices[v])
        
        # Update all occurrences of v to u
        for neighbor in self.vertices[v]:
            # Replace v with u in neighbor's adjacency list
            self.vertices[neighbor] = [u if x == v else x for x in self.vertices[neighbor]]
            # Remove self-loops for the neighbor
            self.vertices[neighbor] = [x for x in self.vertices[neighbor] if x != neighbor]
        
        # Remove self-loops from u's adjacency list
        self.vertices[u] = [x for x in self.vertices[u] if x != u]
        
        # Remove vertex v
        del self.vertices[v]
        
        # Rebuild edge list
        self._build_edges()
    
    def random_contraction(self):
        """Perform random contraction until 2 vertices remain"""
        while len(self.vertices) > 2:
            # Pick random edge
            if not self.edges:
                break
            edge = random.choice(self.edges)
            u, v = edge
            
            # Contract the edge
            self.contract(u, v)
        
        # Return the cut size (number of edges between the last 2 vertices)
        if len(self.vertices) == 2:
            v1, v2 = list(self.vertices.keys())
            return len(self.vertices[v1])
        return 0

def read_graph(filename):
    """Read adjacency list from file"""
    vertices = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = list(map(int, line.strip().split('\t')))
            vertex = parts[0]
            neighbors = parts[1:]
            vertices[vertex] = neighbors
    return Graph(vertices)

def karger_min_cut(graph, trials=None):
    """
    Run Karger's algorithm multiple times to find min cut
    For n vertices, need O(n² log n) trials for high probability
    """
    n = len(graph.vertices)
    if trials is None:
        trials = n * n * int(math.log(n))  # O(n² log n) trials
    
    min_cut = float('inf')
    
    for i in range(trials):
        # Create a fresh copy of the graph for each trial
        g_copy = copy.deepcopy(graph)
        cut = g_copy.random_contraction()
        
        if cut < min_cut:
            min_cut = cut
            print(f"Trial {i+1}: Found new min cut = {cut}")
        
        # Progress indicator
        if (i + 1) % 100 == 0:
            print(f"Completed {i+1}/{trials} trials")
    
    return min_cut

# Main execution
if __name__ == "__main__":
    # Read the graph from file
    filename = "karger_min_cut.txt"  
    print(f"Reading graph from {filename}...")
    graph = read_graph(filename)
    
    print(f"Graph loaded: {len(graph.vertices)} vertices, {len(graph.edges)} edges")
    
    # Run Karger's algorithm
    print("\nRunning Karger's randomized contraction algorithm...")
    min_cut = karger_min_cut(graph, trials=200)  # Start with fewer trials for testing
    
    print(f"\nMinimum cut found: {min_cut}")
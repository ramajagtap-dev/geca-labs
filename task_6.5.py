# Task 6.5: Building MST using Kruskal’s Algorithm
# -------------------------------------------------
# Write Kruskal’s algorithm using edges list and union-find.
# Iterate over sorted edges, add edge if it doesn’t form a cycle.

# Example:
# Graph: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
# Expected MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# MST weight = 19

# Hint: Use union-find to check cycle.
# Tip: Keep track of total weight and chosen edges.


def kruskal_mst(edges, num_vertices):
    """
    Constructs MST using Kruskal's algorithm.
    
    Parameters:
    edges : list of tuples
        Each tuple (u, v, w) represents an edge
    num_vertices : int
        Number of vertices in the graph
        
    Returns:
    mst_edges : list of tuples
        Edges included in MST
    total_weight : int
        Total weight of MST
    """
    # --- Step 1: Sort edges by weight ---
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    # --- Step 2: Initialize union-find ---
    parent = [i for i in range(num_vertices)]
    
    mst_edges = []
    total_weight = 0
    
    # --- Step 3: Iterate over edges ---
    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):  # If adding edge does not form cycle
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w
    
    return mst_edges, total_weight


# --- Helper functions for union-find ---
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x


# --- Example Usage ---
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
num_vertices = 4

mst_edges, mst_weight = kruskal_mst(edges, num_vertices)
print("MST edges:", mst_edges)
print("Total MST weight:", mst_weight)

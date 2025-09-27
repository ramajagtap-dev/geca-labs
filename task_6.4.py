# Task 6.4: Find and Union Functions
# -----------------------------------
# Extend union-find with:
# 1. find(x) -> returns root parent of x.
# 2. union(x, y) -> merges sets containing x and y.

# Example:
# parent = [0,1,2,3]
# union(0,1) → parent updated
# find(1) → should return 0 after union

# Hint: Use recursion for find().
# Tip: Try multiple unions, like (0,1), (1,2).

def find(parent, x):
    """
    Finds the root parent of x recursively.
    
    Parameters:
    parent : list
        Parent array
    x : int
        Vertex to find root for
        
    Returns:
    int : root parent of x
    """
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    """
    Merges the sets containing x and y.
    
    Parameters:
    parent : list
        Parent array
    x, y : int
        Vertices to union
    """
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x  # Merge y into x's set


# --- Example Usage ---
parent = [0, 1, 2, 3]

union(parent, 0, 1)
print("Parent after union(0,1):", parent)
print("Find(1):", find(parent, 1))  

union(parent, 1, 2)
print("Parent after union(1,2):", parent)
print("Find(2):", find(parent, 2))  


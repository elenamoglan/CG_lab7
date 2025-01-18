import networkx as nx
import matplotlib.pyplot as plt

# Define the points of the hexagon
points = {
    "A": (0, 1),
    "B": (0.87, 0.5),
    "C": (0.87, -0.5),
    "D": (0, -1),
    "E": (-0.87, -0.5),
    "F": (-0.87, 0.5),
}

# Define the edges of the triangulation
edges = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F"),
    ("F", "A"),  # Hexagon edges
    ("A", "C"),
    ("C", "E"),
    ("E", "A"),
    ("A", "D"),  # Diagonals to form triangles
]

# Define the subset edges for the 4-point subset triangulation (4 edges)
subset_edges = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "A"),  # Convex hull edges
    ("A", "C"),  # One diagonal
]

# Create graphs
G_full = nx.Graph()
G_full.add_edges_from(edges)

G_subset = nx.Graph()
G_subset.add_edges_from(subset_edges)

# Positions for the nodes
pos = points

# Plot the full triangulation
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
nx.draw(
    G_full,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=500,
    font_weight="bold",
)
plt.title("Full Triangulation (10 Edges)")

# Plot the subset triangulation
plt.subplot(1, 2, 2)
nx.draw(
    G_subset,
    pos,
    with_labels=True,
    node_color="lightgreen",
    node_size=500,
    font_weight="bold",
)
plt.title("Subset Triangulation (4 Edges)")

plt.show()

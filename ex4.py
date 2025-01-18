import networkx as nx
import matplotlib.pyplot as plt

# Define the points of the heptagon
points = {
    "A": (0, 1),
    "B": (0.87, 0.5),
    "C": (0.87, -0.5),
    "D": (0, -1),
    "E": (-0.87, -0.5),
    "F": (-0.87, 0.5),
    "G": (0, 0),  # Center point
}

# Define the edges of the triangulation
edges = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F"),
    ("F", "A"),  # Heptagon edges
    ("A", "C"),
    ("C", "E"),  # Diagonals to form triangles
    ("A", "G"),
    ("C", "G"),
    ("E", "G"),  # Diagonals to the center point
]

# Create the graph
G = nx.Graph()
G.add_edges_from(edges)

# 3-color the graph
colors = nx.coloring.greedy_color(G, strategy="largest_first")
unique_colors = len(set(colors.values()))

# Map colors to a matplotlib colormap
color_map = [plt.cm.tab10(colors[node] / unique_colors) for node in G.nodes]

# Draw the graph using defined positions
nx.draw(
    G,
    pos=points,
    with_labels=True,
    node_color=color_map,
    node_size=500,
    font_color="white",
    font_weight="bold",
)
plt.title("Triangulation of 7 Points with 11 Edges (3-Colorable)")
plt.show()

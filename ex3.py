import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the points for the triangulation
points = np.array(
    [
        [0, 0],  # Point A (0,0)
        [1, 0],  # Point B (1,0)
        [1, 1],  # Point D (1,1)
        [0.5, 0.5],  # Point E (0.5, 0.5) - interior point
    ]
)

# Define the edges for the triangulation (5 edges for 3 triangles)
edges = [
    (0, 1),  # Edge AB
    (1, 2),  # Edge BD
    (2, 0),  # Edge AD
    (1, 3),  # Edge BE
    (2, 3),  # Edge DE
]

# Create a graph
G = nx.Graph()
G.add_edges_from(edges)

# Set up the plot
fig, ax = plt.subplots()
ax.set_aspect("equal")

# Plot the points
ax.scatter(points[:, 0], points[:, 1], color="red")

# Plot the edges
for start, end in edges:
    ax.plot(
        [points[start, 0], points[end, 0]],
        [points[start, 1], points[end, 1]],
        color="black",
    )

coloring = nx.coloring.greedy_color(G, strategy="largest_first")

color_map = {0: "lightblue", 1: "lightgreen", 2: "lightcoral"}

for node, color in coloring.items():
    ax.scatter(
        points[node, 0], points[node, 1], color=color_map[color], s=100, zorder=5
    )
    ax.text(
        points[node, 0],
        points[node, 1],
        f"{chr(65+node)}",
        fontsize=12,
        ha="right",
        zorder=10,
    )

# Title and labels
ax.set_title("Triangulation with 3 Triangles and 5 Edges")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Show the plot
plt.grid(True)
plt.show()

# Check if the graph is 3-colorable (planar graphs with fewer than 4 nodes are 3-colorable)
print("Vertex Coloring:", coloring)

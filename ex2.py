import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the vertices of the polygon
polygon = [(0, 5), (3, -2), (-1, -2), (3, 0), (1, 2), (3, 2)]

# Triangulation for two cameras
triangles_two_cameras = [
    [(0, 5), (3, -2), (1, 2)],
    [(3, -2), (-1, -2), (1, 2)],
    [(1, 2), (-1, -2), (3, 0)],
    [(1, 2), (3, 0), (3, 2)],
]

# Plot the triangulated polygon
fig, ax = plt.subplots()
polygon_patch = patches.Polygon(polygon, closed=True, fill=None, edgecolor="r")
ax.add_patch(polygon_patch)
for triangle in triangles_two_cameras:
    triangle_patch = patches.Polygon(
        triangle, closed=True, fill=None, edgecolor="b", linestyle="--"
    )
    ax.add_patch(triangle_patch)

# Add camera markers
camera_positions = [(0, 5), (1, 2)]
for camera_position in camera_positions:
    ax.plot(camera_position[0], camera_position[1], "go", markersize=10, label="Camera")

# Set plot limits and aspect ratio
ax.set_xlim(-2, 4)
ax.set_ylim(-3, 6)
plt.gca().set_aspect("equal", adjustable="box")

# Add legend
plt.legend()

# Show plot
plt.show()

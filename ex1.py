import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the polygon
vertices = np.array(
    [
        [4, -4],
        [-5, 6],
        [6, -4],
        [-7, 4],
        [9, 6],
        [11, 6],
        [11, -6],
        [9, -6],
        [-7, -4],
        [6, 4],
        [-5, -6],
        [4, 4],
    ]
)

# Plot the polygon
plt.figure()
plt.fill(vertices[:, 0], vertices[:, 1], edgecolor="black", fill=False)

# Place cameras at selected vertices
camera_positions = [vertices[1], vertices[4], vertices[7], vertices[10]]
camera_labels = ["C1", "C2", "C3", "C4"]

# Plot the cameras
for i, pos in enumerate(camera_positions):
    plt.plot(pos[0], pos[1], "ro")  # 'ro' means red color, circle marker
    plt.text(pos[0], pos[1], camera_labels[i], fontsize=12, ha="right")

# Set plot limits and show the plot
plt.xlim(-10, 15)
plt.ylim(-10, 10)
plt.gca().set_aspect("equal", adjustable="box")
plt.title("Polygon with Camera Placements")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from quaternion import Quaternion

"""
    In this iteration, I was able to create a single plot toggling between the original unit cube
    and the rotated unit cube.
"""

# Define cube vertices (global coordinates)
cube_vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
])

# Create a rotation quaternion
axis = np.array([0, 1, 0])  # Y-axis
angle_rad = np.radians(45)  # 45 degrees to radians
rotation_quaternion = Quaternion(np.cos(angle_rad / 2), *np.sin(angle_rad / 2) * axis)

# Apply quaternion rotation to cube vertices, which rotates the cube by 45 degrees ccw about the y-axis
rotated_cube_vertices = []
for vertex in cube_vertices:
    rotated_vertex_quat = rotation_quaternion.rotate_point(vertex)
    rotated_cube_vertices.append([rotated_vertex_quat.x, rotated_vertex_quat.y, rotated_vertex_quat.z])

def update_plot(frame):
    """
    Plots either the original cube or the rotated cube based on the frame number.
    This function is called at each frame to generate an animation using the FuncAnimation method.
 
    Parameters:
        frame (int): The frame number of the animation.
                    If frame = 0, plot the original cube. Else, plot the rotated cube.
    """

    # Clear previous plot
    ax.cla()

    # Check frame number to plot the coressponding cube
    if frame == 0:
        vertices = cube_vertices
    else:
        vertices = rotated_cube_vertices

    # Define the 6 faces of the cube using the vertices
    cube_faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
                  [vertices[4], vertices[5], vertices[6], vertices[7]],
                  [vertices[0], vertices[1], vertices[5], vertices[4]],
                  [vertices[2], vertices[3], vertices[7], vertices[6]],
                  [vertices[1], vertices[2], vertices[6], vertices[5]],
                  [vertices[0], vertices[3], vertices[7], vertices[4]]]

    # Plot the cube faces
    ax.add_collection3d(Poly3DCollection(cube_faces, alpha=0.8, linewidths=1, edgecolors='k'))

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set plot limits
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

    # Turn off axis
    #plt.axis('off')


# Define the 3D plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the animation
ani = FuncAnimation(fig, update_plot, frames=2, interval=1000, blit=False)

plt.show()
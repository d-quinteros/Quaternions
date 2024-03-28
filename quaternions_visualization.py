import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from quaternion import Quaternion

"""
    In this iteration, I was able to create a plot of a unit cube and a second plot of the
    same unit cube, but rotated by a quaternion object as defined in the Quaternion class
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

def plot_cube(vertices):
    """
    Plots a cube in a 3D space.
 
    Parameters:
        vertices (array): The coordinates of the cube's vertices.
    """
    # Define the 3D plot figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the 8 vertices of the cube
    cube_vertices = vertices

    # Define the 6 faces of the cube using the vertices
    cube_faces = [[cube_vertices[0], cube_vertices[1], cube_vertices[2], cube_vertices[3]],
                  [cube_vertices[4], cube_vertices[5], cube_vertices[6], cube_vertices[7]],
                  [cube_vertices[0], cube_vertices[1], cube_vertices[5], cube_vertices[4]],
                  [cube_vertices[2], cube_vertices[3], cube_vertices[7], cube_vertices[6]],
                  [cube_vertices[1], cube_vertices[2], cube_vertices[6], cube_vertices[5]],
                  [cube_vertices[0], cube_vertices[3], cube_vertices[7], cube_vertices[4]]]

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

# Plot the original cube
plot_cube(cube_vertices)

# Plot the rotated cube
plot_cube(rotated_cube_vertices)
plt.show()
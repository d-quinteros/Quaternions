import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from quaternion import Quaternion

"""
    In this iteration, I was able to create a single plot that animates the rotation
    of the unit cube performed by the quaternion.
"""

# Define cube vertices (global coordinates)
cube_vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
])

# Create a rotation quaternion (example rotation around y-axis by 90 degrees)
axis = np.array([1, 1, 0])  # XY-diagonal, y = x

# Calculate the norm of axis
magnitude = np.linalg.norm(axis)

# Normalize the axis
normalized_axis = axis / magnitude

angle_deg = 90 # Desired angle of roation (in degrees)
angle_rad = np.radians(angle_deg)  # Convert angle from degrees to radians

frames = angle_deg * 2 # DOES NOT WORK FOR ALL CASES. CHANGE 

# Change in angle for each frame
delta_angle = angle_rad / angle_deg # DOES NOT WORK FOR ALL CASES. CHANGE 

def update_plot(frame):
    """
    Plots the cube undergoing the rotation performed by the quaternion object.
    This function is called at each frame to generate an animation using the FuncAnimation method.
 
    Parameters:
        frame (int): The frame number of the animation.
    """

    # Clear previous plot and cube vertices
    ax.cla()
    rotated_cube_vertices = []

    # Define the rotation quaternion
    current_angle =+ delta_angle * frame
    rotation_quaternion = Quaternion(np.cos(current_angle/ 2), *np.sin(current_angle / 2) * normalized_axis)

    # Apply quaternion rotation to cube vertices
    for vertex in cube_vertices:
        rotated_vertex_quat = rotation_quaternion.rotate_point(vertex)
        rotated_cube_vertices.append([rotated_vertex_quat.x, rotated_vertex_quat.y, rotated_vertex_quat.z])
    
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
    plt.axis('off')

# Define the 3D plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the animation
ani = FuncAnimation(fig, update_plot, frames, interval=17, repeat=False, blit=False)

plt.show()